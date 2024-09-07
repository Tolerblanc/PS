import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    answer = 0
    check = set([int(input()) for _ in range(n)])
    for _ in range(m):
        if int(input()) in check:
            answer += 1
    print(answer)
