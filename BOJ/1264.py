import sys
input = sys.stdin.readline
while True:
	answer = 0
	inp = input().rstrip()
	if inp == '#':
		break
	for i in inp:
		if i in 'aeiouAEIOU':
			answer += 1
	print(answer)