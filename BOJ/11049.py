import sys
input = sys.stdin.readline

n = int(input())
matrix = []
dp = [[0] * n for _ in range(n)]
for _ in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n - 1):
    dp[i][i + 1] = matrix[i][0] * matrix[i][1] * matrix[i+1][1]

# 왼쪽 위에서 오른쪽 아래 방향으로 연산 진행
for d in range(2, n): # 인덱스 간격
    for i in range(n-d): # 대각선 순회를 위한 인덱스
        # a / bcd ... 부터 ab... / z  까지 연산 하여 가장 작은 것 채워넣기
        # a / bcd ... 로 초기화
        dp[i][i+d] = dp[i+1][i+d] + matrix[i][0] * matrix[i][1] * matrix[i+d][1]
        for k in range(1, d):
            dp[i][i+d] = min(dp[i][i+d], dp[i][i+k] + dp[i+k+1][i+d] + matrix[i][0] * matrix[i+k][1] * matrix[i+d][1])

print(dp[0][-1])