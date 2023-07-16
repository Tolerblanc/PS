import sys

#sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)


n = int(input().rstrip())

graph_rgb = [[] for _ in range(n)]
graph_rb = [[] for _ in range(n)]

for i in range(n):
    inp = input().rstrip()
    for j in inp:
        if j == 'R':
            graph_rgb[i].append(1)
            graph_rb[i].append(1)
        elif j == 'G':
            graph_rgb[i].append(2)
            graph_rb[i].append(1)
        else:
            graph_rgb[i].append(3)
            graph_rb[i].append(3)

def dfs(x, y, graph, target):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == target:
        graph[x][y] = -1
        dfs(x - 1, y, graph, target)
        dfs(x + 1, y, graph, target)
        dfs(x, y + 1, graph, target)
        dfs(x, y - 1, graph, target)
        return True
    return False

result_rgb = 0
result_rb = 0
for i in range(1, 4):
    for x in range(n):
        for y in range(n):
            if dfs(x, y, graph_rgb, i):
                result_rgb += 1
            if i != 2 and dfs(x, y, graph_rb, i):
                result_rb += 1

print(result_rgb, result_rb)