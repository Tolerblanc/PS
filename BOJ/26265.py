from collections import defaultdict
import sys
input = sys.stdin.readline

pairs = defaultdict(list)
for _ in range(int(input())):
    k, v = input().split()
    pairs[k].append(v)

for k, v in sorted(pairs.items()):
    v.sort(reverse=True)
    for n in v:
        print(k, n)
