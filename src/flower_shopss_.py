import csv
from collections import defaultdict, deque


# Breadth_First_Search uses a queue to keep track of visited nodes and searches for paths from source to sink
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
    """
     Finds the maximum flow using the Ford-Falkerson algorithm.

     Parameters:
         graph: dictionary
         source:
         sink: The sink of the stream.

     Returns:
      Find the maximum number of cars that can drive from flower farms to flower shops
      using the Ford-Falkerson algorithm.
     """
    parent = {}
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float('Inf')
        current_node = sink
        while current_node != source:
            path_flow = min(path_flow, graph[parent[current_node]][current_node])
            current_node = parent[current_node]
        max_flow += path_flow
        previous_vertex = sink
        while previous_vertex != source:
            previous_node = parent[previous_vertex]
            graph[previous_node][previous_vertex] -= path_flow
            previous_vertex = previous_node
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


#I would recommend adding an exception
#The try-except construct is used to catch possible exceptions when working with the file and reading the CSV.
#If the file is not found, an error message is displayed.
#If an error occurs while reading the CSV file, an error message is displayed.
#If an unexpected error occurs, an unexpected error message is displayed.
"""
def read_graph_from_csv(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            farms = next(reader)[0].split()
            stores = next(reader)[0].split()
            graph = defaultdict(dict)
            for row in reader:
                from_node, to_node, capacity = row[0].split()
                graph[from_node][to_node] = int(capacity)
        return graph, farms, stores
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None, None, None
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
        return None, None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None, None
"""


if __name__ == "__main__":
    print(maximum_flower_delivery(r'D:\унік\гіти\algo_labs_pt2\tests\roads.csv'))
#change root folders names унік = university; гіти = gits
