import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()
i = 0
answer = 0
while i < n:
    if string[i] == '2':
        left = i
        while i < n and string[i] == '2':
            i += 1
        k = i - left
        answer += k * (k + 1) * (k + 2) // 6
    i += 1
print(answer)
