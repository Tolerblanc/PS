def l2(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        dist = 1e9
        if x != startX:
            dist = min(dist, l2(startX, startY, x, -y), l2(startX, startY, x, n + (n - y)))
            if startX < x:
                dist = min(dist, l2(startX, startY, -x, y))
            if startX > x:
                dist = min(dist, l2(startX, startY, m + (m - x), y))
        if y != startY:
            dist = min(dist, l2(startX, startY, -x, y), l2(startX, startY, m + (m - x), y))
            if startY < y:
                dist = min(dist, l2(startX, startY, x, -y))
            if startY > y:
                dist = min(dist, l2(startX, startY, x, n + (n - y)))
        answer.append(dist)
    return answer