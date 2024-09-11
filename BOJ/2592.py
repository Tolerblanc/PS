from collections import Counter
import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(10)]
counter = Counter(nums)
nums.sort(key=lambda x: -counter[x])
print(sum(nums) // 10)
print(nums[0])
