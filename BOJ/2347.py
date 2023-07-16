import sys

input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
weights.sort()
measureable = 0
for i in range(n):
    if measureable + 1 >= weights[i]:
        measureable += weights[i]
    else:
        break
print(measureable + 1)