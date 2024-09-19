import sys
input = sys.stdin.readline


class AntTunnel():
    def __init__(self):
        self.graph = {}

    def insert(self, n, nodes):
        if nodes[0] not in self.graph:
            self.graph[nodes[0]] = {}
        curr = self.graph[nodes[0]]
        for i in range(1, n):
            if nodes[i] not in curr:
                curr[nodes[i]] = {}
            curr = curr[nodes[i]]

    def dfs(self, depth, curr=None):
        if depth == 0:
            curr = self.graph
        if not curr:
            return
        for node in sorted(curr.keys()):
            print('--' * depth + node)
            self.dfs(depth + 1, curr[node])


antTunnel = AntTunnel()
for _ in range(int(input())):
    n, *nodes = input().split()
    antTunnel.insert(int(n), nodes)

antTunnel.dfs(0)
