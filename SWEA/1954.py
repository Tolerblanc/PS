dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(int(input())):
    n = int(input())
    if n == 1:
        print(f'#{tc + 1}\n1')
        continue
    snail = [[0] * n for _ in range(n)]
    r = c = d = 0
    v = 1
    while snail[r][c] == 0:
        snail[r][c] = v
        v += 1
        r, c = r + dr[d], c + dc[d]
        if r < 0 or c < 0 or r >= n or c >= n or snail[r][c] != 0:
            r, c = r - dr[d], c - dc[d]
            d = (d + 1) % 4
            r, c = r + dr[d], c + dc[d]
    print(f'#{tc + 1}')
    for s in snail:
        print(*s)
