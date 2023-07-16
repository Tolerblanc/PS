import sys

input = sys.stdin.readline

n = int(input())
conferences = []
for _ in range(n):
    start, end = map(int, input().split())
    conferences.append((end, start))
conferences.sort()

time = 0
result = 0
for con in conferences:
    end, start = con
    if start >= time:
        time = end
        result += 1
print(result)