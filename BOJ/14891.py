import sys
from collections import deque
#sys.stdin = open('input.txt')
input = sys.stdin.readline

gears = []

def clockwise(gear):
	lsb = 1 if (gear & 1) else 0
	gear = gear >> 1
	gear += lsb * (2 ** 7)
	return gear

def counterclockwise(gear):
	msb = 1 if (gear & 2 ** 7) else 0
	gear = gear << 1
	gear -= gear & 2 ** 8
	gear += msb
	return gear

def check_spin(left, right):
	left_bit = 1 if (left & 2 ** 5) > 0 else 0
	right_bit = 1 if (right & 2 ** 1) > 0 else 0
	return True if left_bit != right_bit else False

def get_available(gears, target, direction):
	visited = [False] * 4
	result = []
	result.append((target, direction))
	visited[target] = True
	q = deque([(target, direction)])
	while (len(q) != 0):
		t, d = q.pop()
		if (0 <= t + 1 <= 3) and check_spin(gears[t], gears[t + 1]) and not visited[t + 1]: #t + 1 번째 톱니가 회전 가능
			result.append((t + 1, -d))
			visited[t + 1] = True
			q.append((t + 1, -d))
		if (0 <= t - 1 <= 3) and check_spin(gears[t - 1], gears[t]) and not visited[t - 1]: #t - 1 번째 톱니가 회전 가능 
			result.append((t - 1, -d))
			visited[t - 1] = True
			q.append((t - 1, -d))
	return result

def spin(gears, lst):
	for num, direction in lst:
		if (direction == 1):
			gears[num] = clockwise(gears[num])
		else:
			gears[num] = counterclockwise(gears[num])

for _ in range(4):
	gears.append(int(input().rstrip(), base=2))
n = int(input().rstrip())
for i in range(n):
	num, direction = map(int, input().split())
	spin(gears, get_available(gears, num - 1, direction))

answer = 0
for i in range(4):
	if (gears[i] & 2 ** 7):
		answer += 1 * (2 ** i)
print(answer)