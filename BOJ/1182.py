import sys

input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))
result = 0
prefix = 0

def backtracking(cnt):
    global prefix, result
    if cnt == n:
        return
    if lst[cnt] + prefix == s:
        result += 1
    backtracking(cnt + 1) #pass current value
    prefix += lst[cnt]
    backtracking(cnt + 1) #include current value
    prefix -= lst[cnt]

backtracking(0)
print(result)