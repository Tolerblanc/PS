import sys

#sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

down = [False] * (2*n - 1) # row - col + n = index
flag = [False] * 2*n

answer = 0
answer2 = 0
temp = 0
def backtracking(cnt):
    global answer, answer2
    if cnt >= (2*n - 1):
        answer2 = max(answer, answer2)
        return
    start = 0 if cnt < n else cnt - n + 1
    for i in range(start, min(cnt + 1, n)): 
        if graph[i][cnt - i] == 0 or down[2 * i - cnt + n - 1]:
            continue
        down[2 * i - cnt + n - 1] = True
        answer += 1
        flag[cnt] = True
        backtracking(cnt + 2)
        down[2 * i - cnt + n - 1] = False
        answer -= 1
        flag[cnt] = False
    if flag[cnt] == False:
        backtracking(cnt + 2)
backtracking(0)
temp = answer2
answer2 = 0
backtracking(1)
print(temp + answer2)