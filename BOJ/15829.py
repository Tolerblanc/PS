import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()
h = 0
for i, s in enumerate(string):
    h += (ord(s) - ord('a') + 1) * (31 ** i)
print(h % 1234567891)
