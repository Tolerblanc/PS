import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

def check(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append('(')
        elif s == '[':
            stack.append('[')
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(1)
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(1)
                break
    if stack == []:
        print('yes')
    else:
        print('no')

while True:
    string = input().rstrip()
    if string == '.':
        break
    else:
        check(string)