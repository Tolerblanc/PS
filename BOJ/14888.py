import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
nums = input().split()
inp = list(map(int, input().split()))
temp = ['+', '-', '*', '/']
acc = []
for i in range(4):
    for _ in range(inp[i]):
        acc.append(temp[i])

acc = list(set(list(permutations(acc, n - 1))))
v = []
maxV = -int(1e9)
minV = int(1e9)

for a in acc:
    string = nums[0]
    value = 0
    for i in range(1, n):
        value = int(eval(string + a[i - 1] + nums[i]))
        string = str(value)
    maxV = max(maxV, value)
    minV = min(minV, value)
    v.append(value)
print(maxV)
print(minV)