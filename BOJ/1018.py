import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
answer = int(1e9)
black_first = 'BWBWBWBW'
white_first = 'WBWBWBWB'


def check(lr, lc):
    global answer
    bf, wf = 0, 0
    for i in range(lr, lr + 8, 2):  # 0 2 4 6
        bf += sum([o != d for o, d in zip(board[i][lc:], black_first)])
        wf += sum([o != d for o, d in zip(board[i][lc:], white_first)])
    for i in range(lr + 1, lr + 8, 2):  # 1 3 5 7
        bf += sum([o != d for o, d in zip(board[i][lc:], white_first)])
        wf += sum([o != d for o, d in zip(board[i][lc:], black_first)])
    answer = min(answer, bf, wf)


for i in range(n - 7):
    for j in range(m - 7):
        check(i, j)

print(answer)
