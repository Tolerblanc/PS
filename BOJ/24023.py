import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

left = curr = 0
for i in range(n):
    if (k | nums[i]) > k:
        curr = 0
        left = i + 1
        continue
    curr |= nums[i]
    if curr == k:
        print(left + 1, i + 1)
        exit()
print(-1)
