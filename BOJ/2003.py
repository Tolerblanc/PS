import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]
nums = set(nums)
answer = 1 if m in nums else 0
for k in nums:
    answer += 1 if k + m in nums else 0
print(answer)
