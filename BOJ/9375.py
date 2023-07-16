import sys

#sys.stdin = open('input.txt')
input = sys.stdin.readline

tc = int(input().rstrip())
for _ in range(tc):
    n = int(input().rstrip())
    dict = {}
    for _ in range(n):
        inp = input().rstrip().split()
        dict[inp[-1]] = dict.get(inp[-1], 0) + 1
    answer = 1
    for v in dict.values():
        answer *= (v + 1)
    print(answer - 1)