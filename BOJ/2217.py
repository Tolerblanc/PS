import sys
input = sys.stdin.readline

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
ropes.sort(reverse=True)

max_weight = ropes[0]
for i, rope in enumerate(ropes):
    curr = (i + 1) * rope
    if max_weight > curr:
        max_weight = max(max_weight, (i * ropes[i - 1]))
    else:
        max_weight = curr
print(max_weight)
