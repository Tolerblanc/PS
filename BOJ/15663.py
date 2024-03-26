import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
pick = []
visited = [False] * len(nums)
true = False


def backtracking(depth):
    if depth == m:
        print(*pick)
        return
    i = 0
    while i < len(nums):
        if visited[i]:
            i += 1
            continue
        visited[i] = True
        pick.append(nums[i])
        backtracking(depth + 1)
        visited[i] = False
        pick.pop()
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 1
        i += 1


backtracking(0)
