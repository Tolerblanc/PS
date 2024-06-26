for tc in range(int(input())):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    prefix = [0]  # 누적합 리스트
    for num in nums:
        prefix.append(prefix[-1] + num)
    maxPart, minPart = -1, int(1e9)
    for i in range(N - M + 1):
        curPart = prefix[i + M] - prefix[i]
        maxPart = max(maxPart, curPart)
        minPart = min(minPart, curPart)
    print(f'#{tc + 1} {maxPart - minPart}')
