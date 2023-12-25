import sys
input = sys.stdin.readline

n = int(input())
parents = list(map(int, input().split()))
root = parents.index(-1)
target = int(input())
parents[target] = -1

tree = [[] for _ in range(len(parents))]
for i, p in enumerate(parents):
    if p == -1:
        continue
    tree[p].append(i)

stack = [child for child in tree[root]]
answer = 0
while stack:
    curr = stack.pop()
    if not tree[curr]:
        answer += 1
        continue
    for child in tree[curr]:
        stack.append(child)
if target == root:
    print(0)
elif not tree[root]:
    print(1)
else:
    print(answer)