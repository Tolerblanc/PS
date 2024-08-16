from collections import Counter
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    print(f'{a} & {b} are {"NOT " if Counter(
        a) != Counter(b) else ""}anagrams.')
