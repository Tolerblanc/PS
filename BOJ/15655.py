import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
visited = [False] * (n + 1)
nums = sorted(map(int, input().split()))


def backtracking(depth):
    if depth == m:
        print(*result)
        return
    for idx, num in enumerate(nums):
        if visited[idx] or (result and result[-1] >= num):
            continue
        visited[idx] = True
        result.append(num)
        backtracking(depth + 1)
        result.pop()
        visited[idx] = False


backtracking(0)
