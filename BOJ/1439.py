import sys

input = sys.stdin.readline

answer1 = 0
string = input()
length = len(string)
i = 0
while i < length:
    if string[i] == '1':
        answer1 += 1
        while i < length and string[i] == '1':
            i += 1
    else:
        i += 1

answer0 = 0
i = 0
while i < length:
    if string[i] == '0':
        answer0 += 1
        while i < length and string[i] == '0':
            i += 1
    else:
        i += 1
print(min(answer1, answer0))