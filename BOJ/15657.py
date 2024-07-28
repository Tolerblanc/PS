import sys
input = sys.stdin.readline

pick = []
n, m = map(int, input().split())
nums = sorted(map(int, input().split()))


def backtracking(start):
    if len(pick) == m:
        print(*pick)
        return
    for i in range(start, n):
        pick.append(nums[i])
        backtracking(i)
        pick.pop()


backtracking(0)
