import sys
input = sys.stdin.readline

N = int(input())
if N <= 2:
    print("NO")
    exit()
print("YES")
if N % 2:
    answer = [0, 3, 1, 2]
    q = [0, 1, 3, 2]
    while len(answer) <= N:
        q[len(answer) % 4] += 4
        answer.append(q[len(answer) % 4])
    print(*answer[1:])
else:
    answer = [1, 2, 4, 3]
    q = [1, 2, 4, 3]
    while len(answer) < N:
        q[len(answer) % 4] += 4
        answer.append(q[len(answer) % 4])
    print(*answer)
