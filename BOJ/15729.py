import sys
input = sys.stdin.readline

n = int(input())
switches = list(map(int, input().split()))
clicked = 0
for i in range(len(switches)):
    if switches[i]:
        clicked += 1
        switches[i] ^= 1
        if i + 1 < len(switches):
            switches[i + 1] ^= 1
        if i + 2 < len(switches):
            switches[i + 2] ^= 1

print(clicked)
