import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
left = 0
right = 0
odd_cnt = 1 if nums[0] % 2 else 0
even_cnt = 1 if not nums[0] % 2 else 0

for left in range(n):
    while odd_cnt <= k:
        answer = max(answer, even_cnt)
        right += 1
        if right >= n:
            break
        if nums[right] % 2:
            odd_cnt += 1
        else:
            even_cnt += 1
    if nums[left] % 2:
        odd_cnt -= 1
    else:
        even_cnt -= 1

print(answer)
