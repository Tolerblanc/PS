import sys
input = sys.stdin.readline

h, w = map(int, input().split())
ans = 0
flag = 0
for _ in range(h):
    for c in input().rstrip():
        if c == '/':
            flag += 1
        elif c == '\\':
            flag += 1
        elif c == '.' and flag % 2:
            ans += 1
print(ans + flag // 2)
