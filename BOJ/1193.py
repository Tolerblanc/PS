import sys
input = sys.stdin.readline

x = int(input())
i = 1
acc = 0
while acc < x:
    acc += i
    i += 1

acc = x - acc + i
if i % 2 != 0:
    print(f'{acc - 1}/{i - acc + 1}')
else:
    print(f'{i - acc + 1}/{acc - 1}')
