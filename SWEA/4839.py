def binary_search(right, target):
    left = 1
    attempts = 0
    while left < right:
        mid = (left + right) // 2
        attempts += 1
        if mid == target:
            return attempts
        if mid > target:
            right = mid
        else:
            left = mid
    return -1


for tc in range(int(input())):
    p, a, b = map(int, input().split())
    a = binary_search(p, a)
    b = binary_search(p, b)
    result = 'A' if a < b else 'B'
    if a == b:
        result = 0
    print(f'#{tc + 1} {result}')
