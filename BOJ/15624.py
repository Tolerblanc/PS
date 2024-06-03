import sys
input = sys.stdin.readline


def fibo(n):
    if n <= 1:
        return n
    prev, curr = 1, 1
    MOD = 1_000_000_007
    for i in range(2, n):
        prev, curr = curr % MOD, (prev + curr) % MOD
    return curr % MOD


print(fibo(int(input())))
