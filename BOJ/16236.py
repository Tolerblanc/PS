import sys
from collections import deque
input = sys.stdin.readline

# N^2 칸에 대해 N^2 번 탐색 => O(N^4), N <= 20
# 자기보다 크면 못 지나감
# 자기랑 같으면 지나가기만 함
# 자기보다 낮아야 먹을 수 있음
# (최단 거리, 최상단, 최좌측), 이동 1초
# 크기 만큼 먹어야 크기++, 초기 크기 2

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
graph = []
for i in range(n):
    inp = list(map(int, input().split()))
    for j in range(n):
        if inp[j] == 9:
            coor = (i, j)  # 아기 상어 좌표 (행, 열)
            inp[j] = 0
    graph.append(inp)

level = 2  # 현재 상어 크기
eaten = 0  # 먹은 물고기 카운트
time = 0  # 이동 시간 카운트


def bfs():
    # 현재 아기상어 위치에서 BFS 진행
    # 먹을 수 있는 물고기의 정보 (거리, 행, 열) 를 리스트에 담고 정렬
    # 리스트의 맨 앞을 뽑아서 그래프와 카운트, 위치 갱신 후 True 리턴
    #   카운트 갱신 시 상어 크기 체크 후 갱신
    # 리스트 길이가 0이라면 False 리턴
    global coor, level, eaten, time
    q = deque([(coor[0], coor[1], 0)])
    fish = []
    visited = [[False] * n for _ in range(n)]
    visited[coor[0]][coor[1]] = True
    while q:
        r, c, d = q.popleft()
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue  # 그래프 바깥
            if visited[nr][nc] or graph[nr][nc] > level:
                continue  # 방문했거나 자기보다 큰 친구
            if visited[nr][nc] == False:  # 처음 가면서
                if graph[nr][nc] != 0 and graph[nr][nc] < level:  # 자기보다 작으면
                    fish.append((d + 1, nr, nc))
                q.append((nr, nc, d + 1))
                visited[nr][nc] = True

    if (len(fish) == 0):
        return False
    fish.sort()
    coor = (fish[0][1], fish[0][2])
    graph[fish[0][1]][fish[0][2]] = 0
    eaten += 1
    time += fish[0][0]
    if level == eaten:
        level += 1
        eaten = 0
    return True


while True:
    if not bfs():
        print(time)
        break
