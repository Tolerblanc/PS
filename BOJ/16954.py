from collections import deque
import sys
input = sys.stdin.readline

graph = deque()
newLine = '.' * 8
for _ in range(8):
    graph.append(input().rstrip())

move = [
    (0, 0),
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, -1),
    (-1, 1),
    (1, 1),
    (-1, -1),
]

prevQ = deque([(7, 0)])
currQ = deque()
visited = set()
while True:
    while prevQ:
        r, c = prevQ.popleft()
        if graph[r][c] == '#':
            continue
        for i in range(9):
            nr, nc = r + move[i][0], c + move[i][1]
            if nr < 0 or nc < 0 or nr >= 8 or nc >= 8:
                continue
            if (nr, nc) in visited or graph[nr][nc] == '#':
                continue
            if nr == 0 and nc == 7:
                print(1)
                exit()
            visited.add((nr, nc))
            currQ.append((nr, nc))
    prevQ = currQ.copy()
    currQ.clear()
    visited.clear()
    if not prevQ:
        print(0)
        exit()
    graph.pop()
    graph.appendleft(newLine)
