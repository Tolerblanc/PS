import sys
input = sys.stdin.readline

n = int(input())
paper = [[False] * 101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = True

answer = 0
for p in paper:
    answer += sum(p)
print(answer)
