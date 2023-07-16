import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000001)

n, p, q = map(int, input().split())

dp = { 0 : 1 }

def get_number(i, p, q):
    tmp = dp.get(i, -1)
    if tmp != -1:
        return tmp
    x = dp.get(int(i/p), -1)
    if x == -1:
        x = get_number(i/p, p, q)
    y = dp.get(int(i/q), -1)
    if y == -1:
        y = get_number(i/q, p, q)
    dp[i] = x + y
    return x + y

print(get_number(n, p, q))