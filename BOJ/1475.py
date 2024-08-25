from math import ceil
import sys

cnt = [0] * 10
for num in input().rstrip():
    cnt[int(num)] += 1
cnt[6] = cnt[9] = ceil((cnt[6] + cnt[9]) / 2)
print(max(cnt))
