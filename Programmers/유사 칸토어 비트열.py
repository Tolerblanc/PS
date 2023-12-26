def check(n):
    if n % 5 == 2:
        return False
    return True if n < 5 else check(n // 5)

def solution(n, l, r):
    answer = 0
    for i in range(l - 1, r):
        if check(i):
            answer += 1
    return answer