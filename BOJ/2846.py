import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
diff = [lst[i] - lst[i - 1] for i in range(1, n)]
answer = tmp = 0
print(diff)
for d in diff:
    if d <= 0:
        answer = max(answer, tmp)
        tmp = 0
    else:
        tmp += d
print(max(answer, tmp))
