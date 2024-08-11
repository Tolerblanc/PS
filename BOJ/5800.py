import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, *lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    print(f'Class {tc + 1}')
    print(f'Max {max(lst)}, Min {min(lst)}, Largest gap {
          max([lst[i] - lst[i+1] for i in range(n - 1)])}')
