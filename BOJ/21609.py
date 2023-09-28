import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
score = 0


def rotation():  # 반시계 90도 회전
    global graph
    graph = [list(l) for l in zip(*graph)][::-1]


def gravity():  # 중력 적용, -1은 움직이지 않음
    global graph
    for col in range(n):
        bottom = n - 1
        for row in range(n - 1, -1, -1):
            if graph[row][col] > -1:  # 비어있지 않고 검은 블록이 아니면
                if bottom != row:  # 지금 위치가 바닥이 아니면 갱신
                    graph[bottom][col] = graph[row][col]
                    graph[row][col] = -2
                bottom -= 1
            if graph[row][col] == -1:  # 검은 블록이면 바로 위가 바닥
                bottom = row - 1


def bfs_find(graph, visited, r, c):
    '''
    (r, c) 에서 BFS 탐색 시작
    방문하지 않았고, 0 또는 시작점의 원소와 같아야 이동
    0(=무지개 블록)의 좌표를 모두 저장해놓고
    탐색이 종료되는 시점에 개수 체크 후 visited 원복
    (그룹 원소 수, 무지개 블록 수) 반환
    그룹이 이뤄지지 않으면 (0, 0) 반환
    '''
    result = 1
    q = deque([(r, c)])
    rainbow = []
    visited[r][c] = True
    while q:
        curr = q.popleft()
        for i in range(4):
            nr, nc = curr[0] + dx[i], curr[1] + dy[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            if visited[nr][nc] == False and graph[nr][nc] in (graph[r][c], 0):
                visited[nr][nc] = True
                result += 1
                q.append((nr, nc))
                if graph[nr][nc] == 0:  # 무지개 블록
                    rainbow.append((nr, nc))
    for y, x in rainbow:
        visited[y][x] = False
    return (result, len(rainbow))


def bfs_elimination(graph, r, c):
    '''
    초기 (r, c) 와 인접하면서 값이 같은 (또는 0인) 블록 모두 제거(-2)
    없앤 블록의 칸 수를 체크하여 (칸 수)^2 반환
    '''
    result = 1
    q = deque([(r, c)])
    target = graph[r][c]
    graph[r][c] = -2
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            if graph[nr][nc] in (0, target):
                graph[nr][nc] = -2
                result += 1
                q.append((nr, nc))
    # print('score+= ', result * result)
    return result * result


def find_biggest_group(graph, visited):
    '''
    일반 블록은 적어도 하나, 모두 같아야 하며
    검은 블록은 X, 무지개 블록은 상관 없음
    블록 총 개수는 2 이상이며, 인접해야함
    기준 블록은 무지개 블록이 아닌 좌상단 블록
    (크기, 무지개 블록 수, 기준 블록의 행, 기준 블록의 열) 내림차순
    그룹이 없다면 (-1, -1), 있으면 기준 블록 좌표 반환
    '''
    groups = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] or graph[i][j] in (-2, -1, 0):
                continue
            found = bfs_find(graph, visited, i, j)
            if found[0] != 1:
                groups.append(found + (i, j))
    if len(groups) == 0:
        return (-1, -1)
    groups.sort(reverse=True)
    # print('groups : ', groups)
    return (groups[0][2], groups[0][3])


def debug(graph):
    for g in graph:
        print(*g)
    print('===============================')


while True:
    visited = [[False] * n for _ in range(n)]
    r, c = find_biggest_group(graph, visited)
    if (r == -1):
        print(score)
        break
    # print(r, c)
    score += bfs_elimination(graph, r, c)
    # print('after elim==========================')
    # debug(graph)
    gravity()
    # print('after gravity=========================')
    # debug(graph)
    rotation()
    # print('after rotation=========================')
    # debug(graph)
    gravity()
    # print('after gravity2=========================')
    # debug(graph)
