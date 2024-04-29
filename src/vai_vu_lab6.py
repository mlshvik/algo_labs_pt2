from typing import List
class Solution:
    def find_parent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    def union(self, b, g):
        b = self.find_parent(b)
        g = self.find_parent(g)
        if b != g:
            if self.rank[b] < self.rank[g]:
                self.parent[b] = g
            elif self.rank[b] > self.rank[g]:
                self.parent[g] = b
            else:
                self.parent[g] = b
                self.rank[b] += 1 
    def number_of_pairs(self, N: int, pairs: List[List[int]]) -> int:
        max_id = max(max(pair) for pair in pairs)
        self.parent = [i for i in range(max_id + 1)]
        self.rank = [0] * (max_id + 1)

        for b, g in pairs:
            self.union(b, g)

        boy_tribes = set()
        girl_tribes = set()

        for b, g in pairs:
            boy_tribes.add(self.find_parent(b))
            girl_tribes.add(self.find_parent(g))

        return len(boy_tribes) * len(girl_tribes)






