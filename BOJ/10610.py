import sys
input = sys.stdin.readline

num = [int(n) for n in input().rstrip()]
if sum(num) % 3 != 0 or 0 not in num:
    print(-1)
    exit()
num.sort(reverse=True)
print(''.join([str(n) for n in num]))
