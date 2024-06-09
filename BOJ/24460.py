import sys
input = sys.stdin.readline

N = int(input())


def divAndConq(n, lst):
    if n == 1:
        return lst[0][0]
    return sorted([divAndConq(n//2, [lst[i][:n//2] for i in range(n//2)]),
                   divAndConq(n//2, [lst[i][n//2:] for i in range(n//2)]),
                   divAndConq(n//2, [lst[i][:n//2] for i in range(n//2, n)]),
                   divAndConq(n//2, [lst[i][n//2:] for i in range(n//2, n)])],
                  reverse=True)[-2]


inp = [list(map(int, input().split())) for _ in range(N)]
print(divAndConq(N, inp))
