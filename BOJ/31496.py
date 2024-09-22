import sys
input = sys.stdin.readline

n, s = input().split()
count = 0
for _ in range(int(n)):
    name, quantity = input().split()
    for word in name.split('_'):
        if s == word:
            count += int(quantity)
            break

print(count)
