import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print('Error')
elif a == b == c == 60:
    print('Equilateral')
elif a != b != c != a:
    print('Scalene')
else:
    print("Isosceles")
