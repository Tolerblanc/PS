def solution(n, s):
    answer = []
    center = s // n
    if center == 0:
        return [-1]
    for _ in range(n - s % n):
        answer.append(center)
    for _ in range(s % n):
        answer.append(center+1)
    return answer
