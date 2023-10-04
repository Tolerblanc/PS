import sys
input = sys.stdin.readline

'''
n by n 격자에서 파이어볼 m개를 발사, 파이어볼을 각각 좌표, 질량, 방향, 속력을 가짐
격자의 양 끝은 연결되어 있음 (1행 에서 위 -> N행, 1열에서 왼쪽 -> N열)
파이어볼은 8방향으로 이동 가능하며, 무조건 속력만큼 이동함. 한 칸에 여려 개 있을 수 있음
이동 후 한 칸에 여러 개의 파이어볼이 있으면 합쳐짐
    질량 : floor(총 질량 / 5) -> 0이면 소멸
    속력 : floor(총 속력 / 총 개수)
    방향이 모두 홀수 or 짝수이면 0246으로 나눠짐. 아니면 1357
'''

moves = {
    0: (-1, 0),
    1: (-1, 1),
    2: (0, 1),
    3: (1, 1),
    4: (1, 0),
    5: (1, -1),
    6: (0, -1),
    7: (-1, -1),
}
fireballs = []

n, m, k = map(int, input().split())
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])


def move(fireball):
    global n
    r, c, m, s, d = fireball
    nr = (r + moves[d][0] * s) % n
    nc = (c + moves[d][1] * s) % n
    return nr, nc


def magic(new_arr, prev_arr, idx_arr):
    if (len(idx_arr) == 1):
        new_arr.append(prev_arr[idx_arr[0]])
        return
    dirs = []
    m = v = 0
    for i in idx_arr:
        r, c, mi, si, di = prev_arr[i]
        dirs.append(di)
        m += mi
        v += si
    m = int(m / 5)
    if (m == 0):
        return
    v = int(v / len(dirs))
    check = sum([d % 2 for d in dirs])
    next_dir = 0 if check == 0 or check == len(dirs) else 1
    for i in range(0, 8, 2):
        new_arr.append([r, c, m, v, i + next_dir])


for _ in range(k):
    graph = [[] for _ in range(n * n)]
    for idx, fireball in enumerate(fireballs):
        r, c = move(fireball)
        fireball[0], fireball[1] = r, c
        graph[r * n + c].append(idx)
    new = []
    for g in graph:
        if len(g) != 0:
            magic(new, fireballs, g)
    fireballs = new

answer = 0
for fireball in fireballs:
    answer += fireball[2]
print(answer)
