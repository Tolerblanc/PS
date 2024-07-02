from collections import Counter
import sys
input = sys.stdin.readline

_ = int(input())
counter = Counter(list(map(int, input().split())))
_ = int(input())
query = list(map(int, input().split()))
print(*[counter[q] for q in query])
