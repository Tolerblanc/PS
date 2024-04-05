from bisect import bisect
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
lis = [0]

for num in nums:
    if num > lis[-1]:
        lis.append(num)
    else:
        lis[bisect(lis, num)] = num

print(len(nums) - (len(lis) - 1))
