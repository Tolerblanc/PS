import sys
input = sys.stdin.readline

n = int(input())
if (n == 1):
    print(1)
else:
    answer = 1
    suffix = 1
    while (answer * 6 + suffix < n):
        suffix += answer * 6
        answer += 1
    print(answer + 1)
