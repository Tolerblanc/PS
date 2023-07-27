import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [-1] * 100001
cnt = [0] * 100001
graph[n] = 0
q = deque([(n, 0)])
while (len(q) != 0):
	prev, cost = q.popleft()
	for curr in ( prev * 2, prev - 1, prev + 1):
		if (curr < 0 or curr > 100000):
			continue
		if graph[curr] == -1 or (graph[curr] != -1 and graph[curr] > cost + 1):
			graph[curr] = cost + 1
			cnt[curr] = 1
			q.append((curr, cost + 1))
		elif (graph[curr] == cost + 1):
			cnt[curr] += 1

if (n == k):
	print(0)
	print(1)
else:
	print(graph[k])
	print(cnt[k])
# 0 3 / 3 1