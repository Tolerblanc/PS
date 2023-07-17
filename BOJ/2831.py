import sys
input = sys.stdin.readline

n = int(input())
male = list(map(int, input().split()))
male.sort()
female = list(map(int, input().split()))

result = 0

male_lower = []
male_upper = []
for m in male:
	if (m < 0):
		male_lower.append(-m)
	else:
		male_upper.append(m)
male_lower.sort()
male_upper.sort()

female_lower = []
female_upper = []
for f in female:
	if (f < 0):
		female_lower.append(-f)
	else:
		female_upper.append(f)
female_lower.sort()
female_upper.sort()

l = h = 0
while (l < len(male_lower) and h < len(female_upper)):
	if (male_lower[l] > female_upper[h]):
		result += 1
		h += 1
		l += 1
	else:
		l += 1

l = h = 0
while (l < len(female_lower) and h < len(male_upper)):
	if (female_lower[l] > male_upper[h]):
		result += 1
		h += 1
		l += 1
	else:
		l += 1

print(result)