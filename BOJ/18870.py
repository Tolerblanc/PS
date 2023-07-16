import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
comp = sorted(list(set(nums)))
for i in range(n):
    print(bisect_left(comp, nums[i]), end = '')
    if i != n - 1:
        print(' ', end = '')