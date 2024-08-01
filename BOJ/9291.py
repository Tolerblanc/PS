import sys
input = sys.stdin.readline


def check(sdoku):
    for row in sdoku:
        if len(set(row)) != 9:
            return "INCORRECT"
    for col in zip(*sdoku):
        if len(set(col)) != 9:
            return "INCORRECT"
    for i in range(3):
        for j in range(3):
            temp = set()
            for r in range(3):
                for c in range(3):
                    temp.add(sdoku[r + i * 3][c + j * 3])
            if len(temp) != 9:
                return "INCORRECT"
    return "CORRECT"


n = int(input())
for tc in range(n):
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'Case {tc + 1}: {check(sdoku)}')
    if tc != n - 1:
        input()
