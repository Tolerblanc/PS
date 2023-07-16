import sys
input = sys.stdin.readline

a, b = map(int, input().split())
oper = 1
while b > a:
    if b % 10 == 1:
        b -= 1
        b = b // 10
    elif b % 2 == 0:
        b = b // 2
    else:
        oper = -1
        break
    oper += 1
if b < a:
    print(-1)
else:
    print(oper)