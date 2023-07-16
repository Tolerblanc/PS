import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

INF = 1001

n = int(input())
a = list(map(int, input().split()))
dp1 = [0] * n #length of lis
dp2 = [INF] * (n + 1) #smallest value of lis
dp2[0] = -INF

#get lis O(nlogn)
for i in range(n):
    temp = bisect_left(dp2, a[i])
    dp2[temp] = min(dp2[temp], a[i])
    dp1[i] = temp

a.reverse() #reverse input list for get lds
dp3 = [0] * n 
dp2 = [INF] * (n + 1) 
dp2[0] = -INF

#get lds O(nlogn)
for i in range(n):
    temp = bisect_left(dp2, a[i])
    dp2[temp] = min(dp2[temp], a[i])
    dp3[i] = temp
dp3.reverse()

bitonic = 0
for i in range(n):
    bitonic = max(bitonic, dp1[i] + dp3[i] - 1)
print(bitonic)