import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
graph.sort()

def two_pointer(left, right, target):
	left = left + 1 if left == target else left
	right = right - 1 if right == target else right
	while (left < right):
		if graph[left] + graph[right] == graph[target]:
			return 1
		elif graph[left] + graph[right] > graph[target]:
			right -= 1
		else:
			left += 1
		left = left + 1 if left == target else left
		right = right - 1 if right == target else right
	return 0

answer = 0
for i in range(n):
	answer += two_pointer(0, n - 1, i)
print(answer)