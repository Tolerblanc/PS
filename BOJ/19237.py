import sys
input = sys.stdin.readline

'''
자신의 위치에 냄새를 뿌림 -> 1초마다 한 칸 옆으로 이동하고, 냄새를 뿌림 (k번 이동 후 사라짐)
이동 : 냄새가 없는 칸 -> 자신의 냄새가 있는 칸 (상어 별 특정 우선순위) 이동 방향 = 보는 방향
한 칸에 여러 상어가 있으면 번호가 가장 작은 상어만 남음 -> 1번만 남을 때까지

1. 현재 상어 위치에 대해 냄새 초기화
2. 모든 칸 냄새 -1
3. 1번 상어부터 차례대로 이동 방향 결정 -> 이동 -> 냄새 갱신
4. 이동 방향 결정
    냄새 없는 칸 체크 후 1개면 이동, 많으면 우선순위 결정, 없으면
    자신의 냄새가 있는 칸 체크 후 1개면 이동, 많으면 우선순위 결정
5. 이동
    sharks, graph 갱신
    graph에 자기보다 번호가 낮은 상어가 있다면 현재 위치 0, sharks에서 제거, m--
6. 냄새 갱신
    현재 상어 위치에 냄새 k, 상어 번호 갱신
m > 1 and time <= 1000 일때까지 2 ~ 6 반복
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
n, m, k = map(int, input().split())
sharks = [None] * (m + 1)  # [(상어 좌표), 방향]
for i in range(n):
    inp = list(map(int, input().split()))
    graph.append(inp)
    for j in range(n):
        if inp[j] != 0:
            sharks[inp[j]] = [(i, j)]

curr_directions = list(map(int, input().split()))
for idx, d in enumerate(curr_directions):
    sharks[idx + 1].append(d)

direction_priority = [None] * (m + 1)  # 상어 별 [[위], [아래], [왼쪽], [오른쪽]] 우선순위
for i in range(1, m + 1):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    direction_priority[i] = temp

smell = [[0] * n for _ in range(n)]
smell_by = [[0] * n for _ in range(n)]


def update_smell():
    global smell, smell_by, sharks
    for i, shark in enumerate(sharks):
        if not shark:
            continue
        smell[shark[0][0]][shark[0][1]] = k
        smell_by[shark[0][0]][shark[0][1]] = i


def reduce_smell():
    global smell, smell_by
    for i in range(n):
        for j in range(n):
            if smell[i][j] > 0:
                smell[i][j] -= 1
                if smell[i][j] == 0:
                    smell_by[i][j] = 0


def get_next_move():
    '''
    상어 리스트를 순회
    1. None이면 continue
    2. 인접한 빈 칸 체크 
    3. 인접한 자신의 냄새 칸 체크
    4. 이동
    '''
    global graph, sharks, smell, smell_by, direction_priority
    # print('in get_next_move -----------')
    # for s in smell_by:
    # print(*s)
    # print('in get_next_move end--------')
    for i, shark in enumerate(sharks):
        if not shark:
            continue
        cnt, dirs = check_nearby(shark)
        # print(f"{i}'s direction : {dirs}")
        if cnt == 0:
            cnt, dirs = check_nearby(shark, i)
        direction = determine_dir(
            dirs, direction_priority[i][shark[1] - 1])  # i번 상어의 현재 방향
        move(i, direction)


def check_nearby(shark, idx=0):
    '''
    shark 주변의 smell_by를 탐색
    blank == False인 경우, 자신의 냄새를 탐색
    가능한 이동 방향 수, [이동 방향] 리턴
    '''
    global smell_by
    directions = []
    coor, _ = shark
    for i in range(4):
        r, c = coor[0] + dx[i], coor[1] + dy[i]
        if r < 0 or c < 0 or r >= n or c >= n:
            continue
        # print(f'{i} : smell_by[{r}][{c}] = {smell_by[r][c]}')
        if smell_by[r][c] == idx:  # 빈 칸 찾기
            directions.append(i + 1)
    # if (idx == 2):
        # print('checking smells nearby 2 : ', *directions)
    return len(directions), directions


def determine_dir(dirs, prior):
    '''
    len(dirs) == 1 이면 dirs[0] 리턴
    prior랑 dirs 비교하여 리턴
    '''
    if len(dirs) == 1:
        return dirs[0]
    for p in prior:
        if p in dirs:
            return p
    # print('cannot determine the direction')
    return -1


def move(i, direction):
    '''
    i번째 상어를 (direction - 1) 으로 이동 후 graph, sharks 갱신
    x < y 에 대해
    y가 x위로 이동하는 상황은 그냥 y를 없애면 됨 (x의 이동이 이미 끝남) m--
    x가 y위로 이동하는 상황은 y가 이동하지 않았기 때문에...... -> 그래프만 갱신하고 sharks에는 그냥 놔둔다?
    '''
    global graph, sharks, m
    curr, _ = sharks[i]
    r, c = curr[0] + dx[direction - 1], curr[1] + dy[direction - 1]
    # 현재 위치에 자신보다 순위가 높은 상어가 없는 경우 (자기만 있는 경우)
    if graph[curr[0]][curr[1]] == i:
        graph[curr[0]][curr[1]] = 0
    if graph[r][c] != 0 and graph[r][c] < i:  # 자신보다 순위가 높은 상어의 땅으로 이동
        sharks[i] = None
        m -= 1
        return
    graph[r][c] = i
    sharks[i] = [(r, c), direction]


time = 0
update_smell()
while m > 1 and time <= 1000:
    get_next_move()
    reduce_smell()
    update_smell()
    time += 1
    # print('=====================')
    # print(m, time)
    # for g in graph:
    # # print(*g)
    # print('---------------------')
    # for s in smell:
    # print(*s)
    # print('---------------------')
    # for s in smell_by:
    # print(*s)
    # print('=====================')
print(-1 if time > 1000 else time)
