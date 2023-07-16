import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    j = int(input())
    board = []
    board.append(list(map(int, input().split())))
    board.append(list(map(int, input().split())))
    if (j >= 2):
        board[0][1] += board[1][0]
        board[1][1] += board[0][0]
    for k in range(2, j):
        board[0][k] += max(board[1][k - 2], board[1][k - 1])
        board[1][k] += max(board[0][k - 2], board[0][k - 1])
    print(max(board[0][-1], board[1][-1]))
