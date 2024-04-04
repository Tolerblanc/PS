import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    maxSum = -1001
    prefix = 0
    for num in nums:
        prefix = max(0, prefix) + num
        maxSum = max(maxSum, prefix)
    print(maxSum)
