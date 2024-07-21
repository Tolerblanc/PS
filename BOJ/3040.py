from itertools import combinations
import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(9)]
for seq in combinations(nums, 7):
    if sum(seq) == 100:
        print(*seq, sep='\n')
        break
