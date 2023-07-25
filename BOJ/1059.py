import sys
input = sys.stdin.readline

L = int(input())
S = list(map(int, input().split()))
N = int(input())

S.sort()
answer = 0
if not N in S:
	upper_bound = 1000
	lower_bound = S[-1] + 1 if S[-1] + 1 < 1000 else 1000
	for i in range(len(S)):
		if (S[i] > N):
			upper_bound = S[i] - 1
			lower_bound = S[i - 1] + 1
			break
	if (lower_bound > upper_bound):
		lower_bound = 1
	answer += upper_bound - lower_bound
	answer += (upper_bound - N) * (N - lower_bound)
print(answer)