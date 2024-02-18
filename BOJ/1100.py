import sys
input = sys.stdin.readline

count = 0
for i in range(8):
    count += sum([1 for idx, c in enumerate(input().strip())
                 if c == 'F' and idx % 2 == i % 2])
print(count)
