import sys
input = sys.stdin.readline

n = int(input())

left = 0
right = n
while left <= right:
    mid = (left + right) // 2
    if mid * mid == n:
        print(mid)
        break
    if mid * mid > n:
        right = mid - 1
    else:
        left = mid + 1
