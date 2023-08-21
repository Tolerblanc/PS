import sys
from bisect import bisect_left

input = sys.stdin.readline

def find_lis(n, seq):
	dp = [0]
	for i, s in enumerate(seq):
		idx = bisect_left(dp, s)
		if idx == len(dp) and dp[-1] < s:
			dp.append(s)
		else:
			dp[idx] = s
	return len(dp) - 1

while True:
	try:
		n = int(input())
		sequence = list(map(int, input().split()))
		print(find_lis(n , sequence))
	except:
		break
