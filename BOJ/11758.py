import sys
input = sys.stdin.readline

p1 = tuple(map(int, input().split()))
p2 = tuple(map(int, input().split()))
p3 = tuple(map(int, input().split()))

cross = ((p2[0] - p1[0]) * (p3[1] - p1[1])) - ((p2[1] - p1[1]) * (p3[0] - p1[0]))
if cross == 0:
	print(0)
elif cross > 0:
	print(1)
else:
	print(-1)