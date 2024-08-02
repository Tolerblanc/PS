import sys
input = sys.stdin.readline

for _ in range(int(input())):
    c = int(input())
    q, d = divmod(c, 25)
    d, n = divmod(d, 10)
    n, p = divmod(n, 5)
    print(q, d, n, p)
