import sys
input = sys.stdin.readline

n = int(input())
expectations = [int(input()) for _ in range(n)]
expectations.sort()
answer = 0
for idx, exp in enumerate(expectations):
    answer += abs(exp - idx - 1)
print(answer)
