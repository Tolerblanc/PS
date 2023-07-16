import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

stack = []
answer = [-1] * n
for i in range(n - 1, -1, -1):
    while len(stack) != 0:
        if lst[i] < stack[-1]:
            answer[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(lst[i])
print(*answer)