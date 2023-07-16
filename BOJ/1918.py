import sys
from string import ascii_uppercase

input = sys.stdin.readline

stack = []
infix = input().rstrip()
answer = ''
prec = {'*' : 3, '/' : 3, '+' : 2, '-' : 2, '(' : 1}

for i in infix:
    if i in ascii_uppercase:
        answer += i
        continue
    if not len(stack):
        stack.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    elif prec[stack[-1]] < prec[i]:
        stack.append(i)
    elif prec[stack[-1]] >= prec[i]:
        while len(stack) and prec[stack[-1]] >= prec[i]:
            answer += stack.pop()
        stack.append(i)
while len(stack):
    answer += stack.pop()
print(answer)