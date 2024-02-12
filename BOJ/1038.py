import sys
input = sys.stdin.readline

nums = [i for i in range(9, -1, -1)]
decreasing = []


def backtracking(curr, depth):
    decreasing.append(curr)
    if depth == 0:
        return
    for i in range(curr % 10):
        backtracking(curr * 10 + i, depth - 1)


for i in range(10):
    backtracking(i, i)

decreasing.sort()
try:
    print(decreasing[int(input())])
except:
    print(-1)
