import sys
input = sys.stdin.readline

while True:
    a, b, c = sorted(map(int, input().split()))
    if a == b == c == 0:
        break
    print('right' if c ** 2 == a ** 2 + b ** 2 else 'wrong')
