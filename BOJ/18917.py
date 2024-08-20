import sys
input = sys.stdin.readline

xor = 0
add = 0

for _ in range(int(input())):
    comm, *arg = input().split()
    if comm == '1':
        add += int(arg[0])
        xor ^= int(arg[0])
    elif comm == '2':
        add -= int(arg[0])
        xor ^= int(arg[0])
    elif comm == '3':
        print(add)
    else:
        print(xor)
