import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []


def backtracking(depth):
    if depth == m:
        print(*result)
        return

    for i in range(1, n + 1):
        if result and result[-1] > i:
            continue
        result.append(i)
        backtracking(depth + 1)
        result.pop()


backtracking(0)
