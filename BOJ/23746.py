import sys
input = sys.stdin.readline

dic = {}
for _ in range(int(input())):
    v, k = input().split()
    dic[k] = v

prev = list(input().rstrip())
for i in range(len(prev)):
    prev[i] = dic[prev[i]]
s, e = map(int, input().split())
print(''.join(prev)[s-1:e])
