import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
lst = input().split()
comb = combinations(lst, l)
answer = []
for pw in comb:
	cnt1 = cnt2 = 0
	for s in pw:
		if s in 'aeiou':
			cnt1 += 1
		else:
			cnt2 += 1
		if (cnt1 >= 1 and cnt2 >= 2):
			answer.append(''.join(sorted(pw)))
			break

print(*sorted(answer), sep='\n')
