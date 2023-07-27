import sys
from math import sqrt
#sys.stdin = open('input.txt')
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
	lst = []
	answer = 0
	x1, y1, x2, y2 = map(int, input().split())
	n = int(input())
	for _ in range(n):
		cx, cy, r = map(int, input().split())
		if (x1 == x2 and y1 == y2):
			continue
		if (sqrt(pow(x1-cx, 2) + pow(y1-cy, 2)) < r and (sqrt(pow(x2-cx, 2) + pow(y2-cy, 2)) < r)):
			continue
		if (sqrt(pow(x1-cx, 2) + pow(y1-cy, 2)) < r):
			answer += 1
		if (sqrt(pow(x2-cx, 2) + pow(y2-cy, 2)) < r):
			answer += 1
	print(answer)
