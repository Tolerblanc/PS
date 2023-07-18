import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [100000] * 100001
start = (n, 0)
graph[n] = 0
q = deque([start])
while (len(q) != 0):
	prev, cost = q.popleft()
	for curr, new in [(prev * 2, cost), (prev + 1, cost + 1), (prev - 1, cost + 1)]:
		if (curr < 0 or curr > 100000):
			continue
		if (graph[curr] > new):
			graph[curr] = new
			q.append((curr, new))
		if (curr == prev * 2):
			cost += 1

print(graph[k])