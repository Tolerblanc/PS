import sys
from collections import deque
input = sys.stdin.readline

string = input()
flag = False
stack = deque()
for s in string:
	if (s == '<'):
		while (len(stack) != 0):
			print(stack.pop(), end='')
		print(s, end='')
		flag = True
	elif (s == '>'):
		print(s, end='')
		flag = False
	elif (flag):
		print(s, end='')
	elif (s == ' ' or s == '\n'):
		while (len(stack) != 0):
			print(stack.pop(), end='')
		if (s == ' '):
			print(s, end='')
	else:
		stack.append(s)


