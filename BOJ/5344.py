import sys
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(gcd(a, b))
