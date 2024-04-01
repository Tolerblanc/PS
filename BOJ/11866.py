from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
result = []
while len(q):
    for _ in range(k - 1):
        q.append(q.popleft())
    result.append(q.popleft())
print(f"<{', '.join(map(str, result))}>")
