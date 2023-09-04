import sys
input = sys.stdin.readline

moves = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (-1, 0),
    'T': (1, 0),
    'RT': (1, 1),
    'LT': (1, -1),
    'RB': (-1, 1),
    'LB': (-1, -1),
}


def move(dir, king_row, king_col, stone_row, stone_col):
    new_king_row = king_row + moves[dir][1]
    new_king_col = king_col + moves[dir][0]
    new_stone_row = stone_row
    new_stone_col = stone_col
    if new_king_row == new_stone_row and new_king_col == new_stone_col:
        new_stone_row = stone_row + moves[dir][1]
        new_stone_col = stone_col + moves[dir][0]
    if new_stone_row <= 0 or new_stone_col <= 0 or new_stone_row > 8 or new_stone_col > 8 or \
            new_king_row <= 0 or new_king_col <= 0 or new_king_row > 8 or new_king_col > 8:
        return king_row, king_col, stone_row, stone_col
    return new_king_row, new_king_col, new_stone_row, new_stone_col


# row col 반대로 씀;;
king, stone, n = input().split()
k_r, k_c = ord(king[0]) - ord('A') + 1, int(king[1])
s_r, s_c = ord(stone[0]) - ord('A') + 1, int(stone[1])
for _ in range(int(n)):
    k_r, k_c, s_r, s_c = move(input().rstrip(), k_r, k_c, s_r, s_c)
print(chr(k_r + ord('A') - 1), k_c, sep='')
print(chr(s_r + ord('A') - 1), s_c, sep='')
