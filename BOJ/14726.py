import sys
input = sys.stdin.readline

for _ in range(int(input())):
    credit = input().rstrip()
    tmp = 0
    for idx, c in enumerate(credit):
        tmp += int(c) if idx % 2 else sum(map(int, str(int(c) * 2)))
    print('F' if tmp % 10 else 'T')
