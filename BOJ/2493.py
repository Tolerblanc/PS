import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
stack = []
answer = []
for i, h in enumerate(lst):
	while (len(stack) != 0 and stack[-1][0] <= h):
		stack.pop()
	answer.append(0 if len(stack) == 0 else stack[-1][1])
	stack.append((h, i + 1))

print(*answer)
