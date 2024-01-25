from collections import deque

dr = {
    0: (1, 0),
    1: (0, 1),
    2: (-1, 0),
    3: (0, -1),
}


def solution(board):
    N = len(board)
    board[0][0] = 1
    q = deque()  # row, col, cost, direction를 담을 큐
    if board[1][0] != 1:
        q.append((1, 0, 100, 0))
    if board[0][1] != 1:
        q.append((0, 1, 100, 1))
    while q:
        row, col, cost, direction = q.popleft()
        for i in range(4):  # 4 방향에 대해
            if abs(i - direction) == 2:
                continue
            nr, nc = row + dr[i][0], col + dr[i][1]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:   # 다음 좌표가 board 바깥이라면
                continue
            if board[nr][nc] == 1:  # 다음 칸이 벽이라면
                continue
            # 다음 칸 가는 비용 갱신
            next_cost = cost + 100
            if direction != i:  # 방향을 틀었을 때
                next_cost += 500
            if board[nr][nc] != 0 and board[nr][nc] + 500 <= next_cost:  # 재방문이며, 방향을 틀어도 이득볼 수 없는 경우
                continue
            board[nr][nc] = next_cost if board[nr][nc] == 0 else min(
                next_cost, board[nr][nc])
            q.append((nr, nc, next_cost, i))
    return board[-1][-1]
