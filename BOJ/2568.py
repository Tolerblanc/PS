import sys
from bisect import bisect
input = sys.stdin.readline

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

lis = 0
lis_idx = [0] * n
lis_value = [500001] * (n + 1)
lis_value[0] = -500001
for idx, (_, num) in enumerate(lines):
    search = bisect(lis_value, num)
    lis_value[search] = min(lis_value[search], num)
    lis_idx[idx] = search
    lis = max(lis, search)

print(n - lis)
answer = []
for i in range(n - 1, -1, -1):
    if lis > 0 and lis_idx[i] == lis:
        lis -= 1
    else:
        answer.append(lines[i][0])
print(*sorted(answer), sep='\n')
