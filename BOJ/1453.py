import sys
input = sys.stdin.readline

_ = int(input())
pc = [False] * 101
answer = 0
for num in map(int, input().split()):
    if pc[num]:
        answer += 1
    pc[num] = True
print(answer)
