import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input().rstrip())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().rstrip().split())))
triangle.reverse()

for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j + 1])

print(triangle[-1][0])