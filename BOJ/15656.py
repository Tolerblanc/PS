import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pick = []
nums = sorted(map(int, input().split()))


def backtracking(depth):
    if depth == m:
        print(*pick)
        return
    for num in nums:
        pick.append(num)
        backtracking(depth + 1)
        pick.pop()


backtracking(0)
