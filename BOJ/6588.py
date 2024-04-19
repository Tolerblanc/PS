import sys
input = sys.stdin.readline

primes = set(range(3, 1000001))
for i in range(2, int(1000000 ** 0.5) + 1):
    primes -= set(range(i * i, 1000001, i))

while True:
    n = int(input())
    if n == 0:
        break
    for p in primes:
        if n - p in primes:
            print(f'{n} = {p} + {n - p}')
            break
