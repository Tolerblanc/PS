import sys

input = sys.stdin.readline

def solution(n, histogram):
    stack = []
    result = 0
    for i in range(n):
        if not stack:
            stack.append((i, histogram[i]))
        elif stack[-1][1] < histogram[i]:
            stack.append((i, histogram[i]))
        else:
            curr = stack.pop()
            height = curr[1]
            while True:
                if stack:
                    width = curr[0] - stack[-1][0]
                else: #stack empty
                    width = curr[0] + 1
                result = max(result, width * height)
                if not stack or stack[-1][1] < histogram[i]:
                    stack.append((i, histogram[i]))
                    break
                height = stack.pop()[1]
    while stack:
        curr = stack.pop()
        if stack:
            width = n - 1 - stack[-1][0]
        else:
            width = n
        result = max(result, width * curr[1])
    print(result)
                
while True:
    n, *hist = map(int, input().split())
    if n == 0:
        break
    solution(n, hist)