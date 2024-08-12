import sys
input = sys.stdin.readline


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for _ in range(int(input())):
    a, b = map(int, input().split())
    tmp = gcd(a, b)
    print(a * b // tmp, tmp)
