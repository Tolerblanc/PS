import sys
input = sys.stdin.readline

for tc in range(int(input())):
    x, y = map(int, input().split())
    print(f'Case {tc + 1}: {x + y}')
