import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())
while (len(s) != len(t)):
	if (t[-1] == 'A'):
		t.pop()
	elif (t[-1] == 'B'):
		t.pop()
		t.reverse()
print(1 if s == t else 0)