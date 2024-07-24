import sys
input = sys.stdin.readline

people = [input().split() for _ in range(int(input()))]
people = sorted([[x[0], int(x[1]), int(x[2]), int(x[3])]
                for x in people], key=lambda x: (x[3], x[2], x[1]))
print(people[-1][0])
print(people[0][0])
