from collections import Counter
import sys
input = sys.stdin.readline

word = input().rstrip()
counter = Counter(word.upper()).most_common(2)
print(counter[0][0] if len(counter) ==
      1 or counter[0][1] != counter[1][1] else '?')
