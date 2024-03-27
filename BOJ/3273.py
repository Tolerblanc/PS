import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()
left, right = 0, len(nums) - 1
count = 0
while left < right:
    if nums[left] + nums[right] == x:
        count += 1
        left += 1
        right -= 1
    elif nums[left] + nums[right] < x:
        left += 1
    else:
        right -= 1
print(count)
