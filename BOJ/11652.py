import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
print(sorted(Counter(lst).most_common(), key=lambda x: (-x[1], x[0]))[0][0])
