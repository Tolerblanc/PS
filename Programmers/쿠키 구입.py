def solution(cookie):
    answer = 0
    for i in range(1, len(cookie)):  # i: 둘째 아들 시작 인덱스
        l, r = i - 1, i  # l: 첫째 아들 시작 인덱스, r: 둘째 아들 끝 인덱스
        left, right = 0, 0  # 첫째 누적합, 둘째 누적합

        while 0 <= l < r < len(cookie):
            left += cookie[l]
            right += cookie[r]
            if left == right:
                answer = max(answer, left)
                l -= 1
                r += 1
            elif left < right:
                l -= 1
                right -= cookie[r]
            else:
                r += 1
                left -= cookie[l]

    return answer
