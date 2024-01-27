import sys
input = sys.stdin.readline


def check(n):
    nums = [int(i) for i in str(n)]
    d = nums[1] - nums[0]
    for i in range(1, len(nums) - 1):
        if nums[i + 1] - nums[i] != d:
            return False
    return True


n = int(input())
cnt = min(n, 99)
for i in range(100, n + 1):
    if check(i):
        cnt += 1
print(cnt)
