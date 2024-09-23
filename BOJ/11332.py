import sys
input = sys.stdin.readline


def check_tle(comp, n, t, l):
    limit = int(1e8) * l
    if comp == 'O(N)':
        return n * t > limit
    if comp == 'O(N^2)':
        return n * n * t > limit
    if comp == 'O(N^3)':
        return n * n * n * t > limit
    if comp == 'O(2^N)':
        return t * (2 ** n) > limit
    cnt = t
    for i in range(1, n + 1):
        cnt *= i
        if cnt > limit:
            return True
    return False


for _ in range(int(input())):
    complexity, n, t, l = input().split()
    if check_tle(complexity, int(n), int(t), int(l)):
        print('TLE!')
    else:
        print('May Pass.')
