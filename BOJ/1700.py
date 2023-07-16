import sys

input = sys.stdin.readline

n, k = map(int, input().split())
tools = list(map(int, input().split()))
mt = []

answer = 0
for i in range(k):
    if tools[i] in mt:
        continue
    if len(mt) < n:
        mt.append(tools[i])
        continue
    check = tools[i:]
    target = -1
    priority = -1
    for j in range(n):
        try:
            temp = check.index(mt[j])
        except:
            temp = 999
        if temp > priority:
            priority = temp
            target = j
    mt[target] = tools[i]
    answer += 1
print(answer)