import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

answer = 0
left, right = 0, 1000000000
while left <= right:
    mid = (left + right) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    if total >= m:
        answer = max(mid, answer)
        left = mid + 1
    else:
        right = mid - 1
print(answer)
