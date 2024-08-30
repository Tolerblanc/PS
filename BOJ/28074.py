import sys
input = sys.stdin.readline

string = set(input().strip())
if all([ch in string for ch in 'MOBIS']):
    print('YES')
else:
    print('NO')
