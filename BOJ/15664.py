import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
check = set()
pick = []


def backtracking(depth, start):
    if depth == m:
        if tuple(pick) not in check:
            check.add(tuple(pick))
            print(*pick)
        return
    for i in range(start, n):
        pick.append(nums[i])
        backtracking(depth + 1, i + 1)
        pick.pop()


backtracking(0, 0)
