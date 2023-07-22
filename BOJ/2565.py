import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
lst = [(0, 0)]
for _ in range(n):
	a, b = map(int, input().split())
	lst.append((a, b))
lst.sort()
dp = [0] * (n + 1)
for i in range(1, n + 1):
	for j in range(i):
		if (lst[i][1] > lst[j][1] and dp[i] <= dp[j]):
			dp[i] = dp[j] + 1

print(n - max(dp))
