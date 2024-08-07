import sys
from functools import cache
input = sys.stdin.readline


@cache
def solve(k, n):
    if k == 0:
        return n
    return sum([solve(k - 1, i) for i in range(1, n + 1)])


for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(solve(k, n))
