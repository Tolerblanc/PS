import sys
input = sys.stdin.readline


def solve(a, b, c, d):
    cnt = 0
    while not (a == b == c == d == a):
        cnt += 1
        a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
    return cnt


while True:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0:
        break
    print(solve(a, b, c, d))
