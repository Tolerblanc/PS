import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
lst = []
for _ in range(n ** 2):
    lst.append(list(map(int, input().split())))
graph = [[0] * (n + 1) for _ in range(n + 1)]


def determine_seat(idx):
    # 비어있는 칸(graph == 0)에서 주변을 체크
    # (좋아하는 학생 수, 비어있는 칸 수, 행 번호, 열 번호)
    seats = []
    # 그래프 순회하면서 빈 칸에서 주변 체크
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] != 0:
                continue
            favor = empty = 0
            for k in range(4):
                r, c = i + dx[k], j + dy[k]
                if r <= 0 or c <= 0 or r > n or c > n:
                    continue
                if graph[r][c] == 0:
                    empty += 1
                elif graph[r][c] in lst[idx][1:]:
                    favor += 1
            seats.append((favor, empty, i, j))

    seats.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    graph[seats[0][2]][seats[0][3]] = lst[idx][0]


def calc_satis():
    # 모든 칸에서 주변을 체크
    # 0 or 10^(좋아하는 학생수 - 1)
    lst.sort()  # idx == 학생 번호 - 1
    result = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            favor = 0
            for k in range(4):
                r, c = i + dx[k], j + dy[k]
                if r <= 0 or c <= 0 or r > n or c > n:
                    continue
                if graph[r][c] in lst[graph[i][j] - 1][1:]:  # 인접한 학생이 현재 칸 학생이 좋아하는 학생인지
                    favor += 1
            result += (10 ** (favor - 1)) if favor else 0
    return result


for i in range(n ** 2):
    determine_seat(i)
print(calc_satis())
