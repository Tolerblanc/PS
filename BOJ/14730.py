import sys
input = sys.stdin.readline

answer = 0
for _ in range(int(input())):
    c, k = map(int, input().split())
    answer += c * k
print(answer)
