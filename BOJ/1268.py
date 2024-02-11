import sys
input = sys.stdin.readline

n = int(input())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))

students = [[False] * n for _ in range(n)]

# i 학년에 j 번 학생이 k 번 학생과 같은 반이었는지?
for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if info[j][i] == info[k][i]:
                students[j][k] = True
                students[k][j] = True

answer = (0, 0)
for idx, student in enumerate(students):
    curr = sum(student)
    if curr > answer[1]:
        answer = (idx, curr)

print(answer[0] + 1)
