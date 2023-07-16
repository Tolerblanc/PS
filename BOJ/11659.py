import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
pSum = [0] * n
pSum[0] = num[0]
for k in range(1, n):
    pSum[k] = pSum[k - 1] + num[k]

answer = []
for _ in range(m):
    i, j = map(int, input().split())
    answer.append(pSum[j - 1] - pSum[i - 1] + num[i - 1])
for a in answer:
    print(a)