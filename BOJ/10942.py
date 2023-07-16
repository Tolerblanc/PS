import sys

sys.setrecursionlimit(int(1e7))
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
dp = [[-1] * n for _ in range(n)]

def solve(start, end):
    if start == end:
        dp[start][end] = 1
    elif end - start == 1:
        if nums[start] == nums[end]:
            dp[start][end] = 1
        else:
            dp[start][end] = 0
    elif nums[start] != nums[end]:
        dp[start][end] = 0
    elif dp[start][end] != -1:
        return dp[start][end]
    else:
        dp[start][end] = solve(start + 1, end - 1)
    return dp[start][end]

m = int(input().rstrip())
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    print(solve(a - 1, b - 1))