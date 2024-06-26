import sys
input = sys.stdin.readline


def fibo(n):
    if n <= 3:
        return n
    prev, curr = 1, 2
    MOD = 15746
    for i in range(2, n):
        prev, curr = curr % MOD, (prev + curr) % MOD
    return curr % MOD


print(fibo(int(input())))
