import sys
input = sys.stdin.readline

for _ in range(int(input())):
    lst = []
    for _ in range(int(input())):
        name, cnt = input().split()
        lst.append((int(cnt), name))
    lst.sort(reverse=True)
    print(lst[0][1])
