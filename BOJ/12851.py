import sys
from collections import deque
input = sys.stdin.readline
INF = 1000001

n, k = map(int, input().split())
time = [INF] * 100001
case = [-1] * 100001
time[n] = 0
case[n] = 1
if (n == k):
	print(0)
	print(1)
else:
	q = deque([(n, 0)])
	while (len(q) != 0):
		prev, cost = q.popleft()
		for curr in (prev * 2, prev - 1, prev + 1):
			if (curr < 0 or curr > 100000):
				continue
			if (time[curr] == cost + 1):
				case[curr] += 1
			elif (time[curr] > cost + 1):
				time[curr] = cost + 1
				case[curr] = case[prev]
				if (curr != k):
					q.append((curr, cost + 1))
	print(time[k])
	print(case[k])

