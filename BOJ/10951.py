import sys
input = sys.stdin.readlines

inp = input()
for i in inp:
    a, b = map(int, i.split())
    print(a + b)
