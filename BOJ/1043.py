import sys

#sys.stdin = open('input.txt')
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
    
def union(parent, nodes):
    pp = find(parent, min(nodes))
    for n in nodes:
        parent[find(parent, n)] = pp
    return pp
        
n, m = map(int, input().rstrip().split())
parent = [x for x in range(n + 1)]
answer = 0

x, *people = map(int, input().rstrip().split())
if x == 0:
    answer = m
else:
    union(parent, people)
    check = []
    for _ in range(m):
        y, *party = map(int, input().rstrip().split())
        if x == 0:
            continue
        check.append(union(parent, party))

    fact = find(parent, min(people))
    for c in check:
        if find(parent, c) == fact:
            continue
        else:
            answer += 1
print(answer)