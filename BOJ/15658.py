import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

max_result = -float('inf')
min_result = float('inf')


def backtracking(depth, curr):
    global max_result, min_result, plus, minus, multiply, divide
    if depth == n:
        max_result = max(max_result, curr)
        min_result = min(min_result, curr)
        return

    if plus > 0:
        plus -= 1
        backtracking(depth + 1, curr + nums[depth])
        plus += 1
    if minus > 0:
        minus -= 1
        backtracking(depth + 1, curr - nums[depth])
        minus += 1
    if multiply > 0:
        multiply -= 1
        backtracking(depth + 1, curr * nums[depth])
        multiply += 1
    if divide > 0:
        divide -= 1
        backtracking(depth + 1, int(curr / nums[depth]))
        divide += 1


backtracking(1, nums[0])
print(max_result)
print(min_result)
