import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())

count = 0
def find(n, r, c):
    global count
    if n == 1:
        if r % 2 == 1 and c % 2 == 1:
            return count + 3
        elif r % 2 == 1 and c % 2 == 0:
            return count + 2
        elif r % 2 == 0 and c % 2 == 1:
            return count + 1
        else:
            return count
    if r >= 2 ** (n - 1) and c >= 2 ** (n - 1): #4
        count += 2 ** (2*n - 2) + 2 ** (2*n - 1)
        r -= 2 ** (n - 1)
        c -= 2 ** (n - 1)
    elif r >= 2 ** (n - 1) and c < 2 ** (n - 1): #3
        count += 2 ** (2*n - 1)
        r -= 2 ** (n - 1) 
    elif r < 2 ** (n - 1) and c >= 2 ** (n - 1): #2
        count += 2 ** (2*n - 2)
        c -= 2 ** (n - 1)
    return find(n - 1, r, c)

print(find(n, r, c))