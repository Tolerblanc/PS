import sys
from bisect import bisect_left

input = sys.stdin.readline

INF = int(1e9 + 1)

n = int(input())
a = list(map(int, input().split()))
dp1 = [0] * n #length of lis
dp2 = [INF] * (n + 1) #smallest value of lis
dp2[0] = -INF
lis = 0

#get lis O(nlogn)
for i in range(n):
    temp = bisect_left(dp2, a[i])
    dp2[temp] = min(dp2[temp], a[i])
    dp1[i] = temp
    lis = max(temp, lis)

answer = []
target = lis
for i in range(n - 1, -1, -1):
    if target <= 0:
        break
    if dp1[i] == target:
        answer.append(a[i])
        target -= 1
        
print(lis)
for i in answer[::-1]:
    print(i, end = ' ')