def solution(sticker):
    if len(sticker) < 2:
        return sticker[0]

    dp1 = [0] * (len(sticker) - 1)  # 맨 처음 스티커를 뜯는다
    dp2 = dp1[:]  # 맨 처음 스티커는 넘기고, 그 다음 스티커를 뜯는다.

    dp1[0], dp2[0] = sticker[0], sticker[1]
    for i in range(1, len(sticker) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i + 1])
    return max(dp1[-1], dp2[-1])
