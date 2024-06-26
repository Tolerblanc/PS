for tc in range(int(input())):
    K, N, M = map(int, input().split())
    prev = curr = 0
    answer = 0
    i = 0
    station = list(map(int, input().split()))

    while curr + K < N:
        prev = curr
        while i < M and station[i] <= curr + K:
            prev = station[i]
            i += 1

        if prev == curr:
            answer = 0
            break
        curr = prev
        answer += 1

    if curr + K < N:
        answer = 0

    print(f'#{tc + 1} {answer}')
