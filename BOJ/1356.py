import sys
input = sys.stdin.readline


def check(string):
    for i in range(1, len(string)):
        left = 1
        right = 1
        for j in range(i):
            left *= int(string[j])
        for j in range(i, len(string)):
            right *= int(string[j])
        if left == right:
            return True
    return False


print('YES' if check(input().strip()) else 'NO')
