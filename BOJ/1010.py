import sys
from math import factorial
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
	k, n = map(int, input().split())
	print(factorial(n) // (factorial(k) * factorial(n - k)))
