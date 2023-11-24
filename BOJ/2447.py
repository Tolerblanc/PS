import sys
input = sys.stdin.readline

N = int(input())


def star(k):
    if k == 3:
        return ['***', '* *', '***']
    prev = star(k // 3)
    return [s * 3 for s in prev] + [s + ' ' * (k // 3) + s for s in prev] + [s * 3 for s in prev]


print(*star(N), sep='\n')
