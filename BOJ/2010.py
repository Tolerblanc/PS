import sys
input = sys.stdin.readline

total = 1
for _ in range(int(input())):
    total += int(input()) - 1
print(total)
