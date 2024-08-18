import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
prefix = [0]
for num in nums:
    prefix.append(prefix[-1] + num)
for _ in range(int(input())):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])
