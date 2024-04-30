import csv
from collections import defaultdict, deque
import unittest
import os


def read_graph_from_csv(file_path):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        farms = next(reader)[0].split()
        stores = next(reader)[0].split()
        graph = defaultdict(dict)
        for row in reader:
            from_node, to_node, capacity = row[0].split()
            graph[from_node][to_node] = int(capacity)
    return graph, farms, stores


def bfs(graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    while queue:
        current = queue.popleft()
        if current == sink:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited and graph[current][neighbor] > 0:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
                if neighbor == sink:
                    return True
    return False


def ford_fulkerson(graph, source, sink):
    parent = {}
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            v = u
    return max_flow


def maximum_flower_delivery(file_path):
    graph, farms, stores = read_graph_from_csv(file_path)
    source = "Source"
    sink = "Sink"
    for farm in farms:
        graph[source][farm] = float('Inf')
    for store in stores:
        graph[store][sink] = float('Inf')
    return ford_fulkerson(graph, source, sink)



