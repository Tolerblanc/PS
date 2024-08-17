import sys
input = sys.stdin.readline


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


numerator1, denominator1 = map(int, input().split())
numerator2, denominator2 = map(int, input().split())

denominator = denominator1 * denominator2
numerator = numerator1 * denominator2 + numerator2 * denominator1

numerator, denominator = numerator // gcd(
    numerator, denominator), denominator // gcd(numerator, denominator)
print(numerator, denominator)
