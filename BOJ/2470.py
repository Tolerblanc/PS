import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

def solve():
	left = 0
	right = n - 1
	answer = (abs(lst[left] + lst[right]), left, right)
	if answer[0] == 0: right = 0
	elif lst[left] + lst[right] < 0 : left += 1
	elif lst[left] + lst[right] > 0 : right -= 1
	while (left < right):
		if abs(lst[left] + lst[right]) < answer[0]:
			answer = (abs(lst[left] + lst[right]), left, right)
		if (lst[left] + lst[right] == 0): break
		elif lst[left] + lst[right] < 0 : left += 1
		elif lst[left] + lst[right] > 0 : right -= 1
	
	print(lst[answer[1]], lst[answer[2]])

solve()
