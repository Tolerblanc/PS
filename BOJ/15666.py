import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))
pick = []


def backtracking(idx, depth):
    if depth == m:
        print(*pick)
        return
    for i in range(idx, len(nums)):
        pick.append(nums[i])
        backtracking(i, depth + 1)
        pick.pop()


backtracking(0, 0)
