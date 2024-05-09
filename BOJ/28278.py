import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    op, *arg = map(int, input().split())
    if op == 1:
        stack.append(arg[0])
    elif op == 2:
        print(stack.pop() if stack else -1)
    elif op == 3:
        print(len(stack))
    elif op == 4:
        print(1 if not len(stack) else 0)
    elif op == 5:
        print(stack[-1] if stack else -1)
