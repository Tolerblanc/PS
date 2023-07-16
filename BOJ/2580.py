import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

graph = [[] for _ in range(9)]
blank = []

#input & init
for i in range(9):
    inp = list(map(int, input().rstrip().split()))
    for j in range(9):
        graph[i].append(inp[j])
        if inp[j] == 0:
            blank.append((i, j))
end = len(blank)
complete = False

#function to check adding value is possible in graph[x][y]
def check(value, x, y):
    #horizontal
    for i in range(9):
        if value == graph[x][i]:
            return False
    #vertical
    for i in range(9):
        if value == graph[i][y]:
            return False
    #3x3 square
    tmp_x = x // 3 * 3
    tmp_y = y // 3 * 3
    for i in range(tmp_x, tmp_x + 3):
        for j in range(tmp_y, tmp_y + 3):
            if value == graph[i][j]:
                return False
    return True

def backtracking(cnt):
    global complete
    if complete:
        return
    if cnt == end:
        for g in graph:
            print(*g)
        complete = True
        return
    x, y = blank[cnt]
    for i in range(1, 10):
        if not check(i, x, y):
            continue    
        graph[x][y] = i
        backtracking(cnt + 1)
    graph[x][y] = 0

backtracking(0)