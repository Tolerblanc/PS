import sys

input = sys.stdin.readline

origin = input().rstrip()
target = input().rstrip()
exp = len(target)
stack = []

for char in origin:
    flag = True
    stack.append(char)
    if len(stack) < exp:
        continue
    for i in range(exp):
        if target[i] != stack[-exp+i]:
            flag = False
            break
    if flag:
        for _ in range(exp):
            stack.pop()

if len(stack) < 1:
    print("FRULA")
else:
    print(''.join(stack))