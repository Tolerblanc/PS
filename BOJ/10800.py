import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
balls = [list(map(int, input().split())) + [i] for i in range(n)]
balls.sort(key=lambda x: (x[1], x[0]))
colors = defaultdict(int)
sizes = defaultdict(int)
answer = [0] * n
total = 0

for i, (color, size, idx) in enumerate(balls):
    colors[color] += size
    sizes[size] += size
    total += size
    answer[idx] = total - colors[color] - sizes[size] + size
    if i > 0 and balls[i-1][1] == size and balls[i-1][0] == color:
        answer[idx] = answer[balls[i-1][2]]

print(*answer, sep='\n')
