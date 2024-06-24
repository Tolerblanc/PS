for tc in range(1, int(input()) + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    print(f'#{tc} {max(nums) - min(nums)}')
