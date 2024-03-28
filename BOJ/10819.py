import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
visited = [False] * len(nums)
answer = 0
pick = []


def backtracking(depth):
    global answer
    if depth == len(nums):
        temp = 0
        for i in range(1, len(nums)):
            temp += abs(pick[i] - pick[i - 1])
        answer = max(answer, temp)
        return

    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            pick.append(nums[i])
            backtracking(depth + 1)
            pick.pop()
            visited[i] = False


backtracking(0)
print(answer)
