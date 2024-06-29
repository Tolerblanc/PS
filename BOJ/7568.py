import sys
input = sys.stdin.readline

people = [tuple(map(int, input().split())) for _ in range(int(input()))]
result = [1] * len(people)
for i in range(len(people) - 1):
    nx, ny = people[i]
    for j in range(i + 1, len(people)):
        px, py = people[j]
        if nx > px and ny > py:
            result[j] += 1
        if nx < px and ny < py:
            result[i] += 1
print(*result)
