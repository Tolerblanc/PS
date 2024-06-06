import sys
input = sys.stdin.readline


def solve(x):
    i = 1
    acc = 0
    while acc < x:
        acc += i
        i += 1

    acc = x - acc + i
    if i % 2 != 0:
        print(f'TERM {x} IS {acc - 1}/{i - acc + 1}')
    else:
        print(f'TERM {x} IS {i - acc + 1}/{acc - 1}')


while True:
    try:
        solve(int(input()))
    except:
        break
