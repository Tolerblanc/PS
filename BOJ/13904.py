import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    limit, score = map(int, input().split())
    lst.append((limit, score))
lst.sort(key=lambda x: (-x[1], x[0]))
days = [True] * 1001  # i일에 과제 가능
total = 0
for d, s in lst:
    for i in range(d, 0, -1):
        if not days[i]:
            continue
        days[i] = False
        total += s
        break

print(total)
