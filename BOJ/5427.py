import sys
from collections import deque
#sys.stdin = open('input.txt')
input = sys.stdin.readline

tc = int(input().rstrip())
tile = {'.' : 0, '#' : 1, '*' : 2, '@' : -1}
for _ in range(tc):
    w, h = map(int, input().rstrip().split())
    graph = []
    player = deque()
    fire = deque()
    for i in range(h):
        temp = [tile[x] for x in input().rstrip()]
        graph.append(temp)
        for j in range(w):
            if temp[j] == 2:
                fire.append((i, j, 0))
            if temp[j] == -1:
                player.append((i, j , 0))
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    last_fire = len(fire)
    last_player = 1
    flag = False
    while not flag:
        if len(player) < 1:
            print('IMPOSSIBLE')
            break
        ff = last_fire
        last_fire = 0
        for i in range(ff):
            fire_now = fire.popleft()
            for i in range(4):
                row = dx[i] + fire_now[0]
                col = dy[i] + fire_now[1]
                if row < 0 or col < 0 or row >= h or col >= w:
                    continue
                if graph[row][col] < 1:
                    graph[row][col] = 2
                    fire.append((row, col, fire_now[2] + 1))
                    last_fire += 1
        pp = last_player
        last_player = 0
        for i in range(pp):
            r, c, t = player.popleft()
            if r == 0 or r == h - 1 or c == 0 or c == w - 1:
                print(t + 1)
                flag = True
                break
            for i in range(4):
                row = dx[i] + r
                col = dy[i] + c
                if row < 0 or col < 0 or row >= h or col >= w:
                    continue
                if graph[row][col] == 0:
                    graph[row][col] = -1
                    player.append((row, col, t + 1))
                    last_player += 1