import sys
input = sys.stdin.readline

for _ in range(int(input())):
    idx, string = input().split()
    idx = int(idx)
    print(string[:idx-1] + string[idx:])
