import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()


def check(s, t):
    if len(s) == len(t):
        return s == t
    if t[0] == 'B' and check(s, t[:0:-1]):
        return True
    if t[-1] == 'A' and check(s, t[:-1]):
        return True


print(1 if check(S, T) else 0)
