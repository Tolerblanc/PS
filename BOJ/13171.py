import sys
input = sys.stdin.readline

A = int(input())
X = int(input())

div_num = 1_000_000_007
answer = 1
cur = A

while X:
    if X & 1:
        answer = (answer * cur) % div_num
    cur = (cur ** 2) % div_num
    X //= 2

print(answer)
