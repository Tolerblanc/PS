import sys
from collections import deque
#sys.stdin = open('input.txt')
input = sys.stdin.readline

moves = {(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)}

tc = int(input())
for _ in range(tc):
	l = int(input())
	curr_x, curr_y = map(int, input().split())
	dest_x, dest_y = map(int, input().split())
	graph = [[-1] * l for _ in range(l)]
	graph[curr_x][curr_y] = 0
	q = deque([(curr_x, curr_y, 0)])
	while (len(q) != 0):
		curr_x, curr_y, cost = q.popleft()
		for dx, dy in moves:
			next_x = curr_x + dx
			next_y = curr_y + dy
			if (next_x < 0 or next_y < 0 or next_x >= l or next_y >= l):
				continue
			if (graph[next_x][next_y] != -1 and graph[next_x][next_y] <= cost + 1):
				continue
			graph[next_x][next_y] = cost + 1
			q.append((next_x, next_y, cost + 1))
		if (graph[dest_x][dest_y] != -1):
			print(graph[dest_x][dest_y])
			break