import sys
input = sys.stdin.readline

n = int(input())

students = [input().rstrip() for _ in range(n)]

for k in range(-1, -len(students[0]) - 1, -1):
    if len(set([int(student[k:]) for student in students])) == len(students):
        print(-k)
        break
