import sys
input = sys.stdin.readline
string = input().rstrip()
print(sum([string.count(c) for c in 'aeiou']))
