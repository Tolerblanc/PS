import sys
from copy import deepcopy
input = sys.stdin.readline

'''
물고기는 번호가 작은 순서대로, 위치 교환식으로 이동
이동할 수 없다면 패스, 그 외의 경우에는 방향을 바꿔가며 최종 이동 결정
상어는 먹은 물고기의 방향을 가지며, 초기에는 (0, 0)에서 시작.
또한 상어는 여러 칸 이동이 가능하다. 먹은 물고기 번호의 합이 최대가 되어야 한다.
'''

graph = [[None] * 4 for _ in range(4)]
fish = [None] * 17  # 먹힌 물고기는 None
directions = {
    1: (-1, 0),
    2: (-1, -1),
    3: (0, -1),
    4: (1, -1),
    5: (1, 0),
    6: (1, 1),
    7: (0, 1),
    8: (-1, 1),
}
answer = 0

for i in range(4):
    inp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        graph[i][j//2] = [inp[j], inp[j + 1]]  # 물고기 번호, 방향
        fish[inp[j]] = (i, j//2)


def determine_direction(graph, fish, idx):
    '''
    현재 idx번 물고기의 위치를 결정하는 함수
    idx 외에 모든 방향을 탐색했을 때, 불가능하다면 (0, 0) 리턴
    탐색 후 방향 튜플 리턴
    '''
    curr_dir = graph[fish[idx][0]][fish[idx][1]][1]
    r, c = fish[idx]
    for i in range(8):
        next_dir = (curr_dir + i) % 8
        if next_dir == 0:
            next_dir = 8
        nr, nc = r + directions[next_dir][0], c + directions[next_dir][1]
        if nr < 0 or nc < 0 or nr >= 4 or nc >= 4:
            continue
        if graph[nr][nc] != None and graph[nr][nc][0] == 0:
            continue
        graph[fish[idx][0]][fish[idx][1]][1] = next_dir
        return directions[next_dir]
    return (0, 0)


def move_fish(graph, fish):
    '''
    1번 부터 15번까지 물고기 위치를 변경하는 함수
    determine 함수로 물고기 좌표를 결정한 후, 해당 위치의 graph 검사
    현재 위치 <-> 다음 위치 교환 후 fish 배열에서도 좌표 교환
    '''
    for idx in range(1, 17):
        if fish[idx] == None:
            continue
        nr, nc = determine_direction(graph, fish, idx)
        if nr == 0 and nc == 0:
            continue
        prev_r, prev_c = fish[idx]
        next_r, next_c = prev_r + nr, prev_c + nc
        if graph[next_r][next_c] != None:
            fish[idx], fish[graph[next_r][next_c][0]] = fish[graph[next_r][next_c][0]], fish[idx]
        else:
            fish[idx] = (next_r, next_c)
        graph[prev_r][prev_c], graph[next_r][next_c] = graph[next_r][next_c], graph[prev_r][prev_c]

def debug(graph, fish, score, x, y):
    print('==================================')
    print(f"curr score : {score}, shark : ({x}, {y})")
    for g in graph:
        print(*g)
    print('----------------------------------')
    print(fish)
    print('==================================')

def simulate(graph, fish, score, x, y):
    '''
    (x, y) 위치로 상어가 이동 후, 나머지 물고기들이 전부 이동
    (x, y) 에서 상어가 이동할 수 있는 경우의 수에 대해 백트래킹 수행
    더이상 백트래킹 시도가 불가능한 상황일 경우, 정답 갱신
    '''
    global answer
    # debug(graph, fish, score, x, y)
    eaten_fish = graph[x][y]
    shark_dir = eaten_fish[1]
    score += eaten_fish[0]
    fish[eaten_fish[0]] = None
    graph[x][y] = [0, shark_dir]
    move_fish(graph, fish)
    graph[x][y] = None
    for i in range(1, 4):
        r, c = x + directions[shark_dir][0] * i, y + directions[shark_dir][1] * i
        if r < 0 or c < 0 or r >= 4 or c >= 4:
            continue
        if graph[r][c] == None:
            continue
        simulate(deepcopy(graph), deepcopy(fish), score, r, c)
    else:
        answer = max(answer, score)


simulate(graph, fish, 0, 0, 0)
print(answer)