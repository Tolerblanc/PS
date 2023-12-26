import sys
input = sys.stdin.readline

n = int(input())

def star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    parts = star(n // 2)
    return [' ' * (n // 2) + s + ' ' * (n // 2) for s in parts] + [s + ' ' + s for s in parts]

print(*star(n), sep='\n')