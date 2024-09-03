import sys
input = sys.stdin.readline

n, k = map(int, input().split())
divisors = [i for i in range(1, n + 1) if n % i == 0]
print(divisors[k - 1] if len(divisors) >= k else 0)
