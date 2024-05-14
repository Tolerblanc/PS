import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
pick = []
answer = set()
visited = [False] * n


def backtracking(depth):
    if depth == m:
        answer.add(tuple(pick))
        return
    for num in nums:
        pick.append(num)
        backtracking(depth + 1)
        pick.pop()


backtracking(0)
for comb in sorted(answer):
    print(*comb)
