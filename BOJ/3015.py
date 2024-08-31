import sys
input = sys.stdin.readline

n = int(input())
people = [int(input()) for _ in range(n)]
stack = []

answer = 0

for height in people:
    count = 1
    # 스택: (나보다 크거나 같은 사람 수 ,키)
    while stack and stack[-1][1] <= height:
        prevCnt, prev = stack.pop()
        answer += prevCnt
        if prev == height:
            count += prevCnt
    if stack:
        answer += 1
    stack.append((count, height))
print(answer, end='')
