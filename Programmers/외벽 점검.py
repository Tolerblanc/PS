from itertools import permutations


def simulate(interval, dist):
    worker = 0  # 친구 인덱스
    acc = 0  # 구간 누적
    idx = 0  # 구간 인덱스
    visited = [False] * len(interval)
    print(f'simulating {interval} with {dist}')
    print(f'worker: {worker}, acc: {acc}, idx: {idx}, visited: {visited}')
    while idx < len(interval) and worker < len(dist):
        acc += interval[idx]
        visited[idx - 1] = True
        if acc < dist[worker]:
            visited[idx] = True
            idx += 1
        elif acc == dist[worker]:
            visited[idx] = True
            acc = 0
            idx += 2
            worker += 1
        else:
            idx += 1
            worker += 1
            acc = 0
        print(f'worker: {worker}, acc: {acc}, idx: {idx}, visited: {visited}')

    return all(visited)


def is_possible_work(interval, dist):
    # 모든 시작점에 대해 현재 dist 조합으로 시뮬레이션
    for start_point, _ in enumerate(interval):
        # 간격으로 시뮬레이션 돌리므로 방향 고려 X
        if simulate(interval[start_point:] + interval[:start_point], dist):
            return True
    return False


def check(interval, dist, friends):
    # friends 명으로 만들 수 있는 모든 dist 조합에 대해, interval을 만족시킬 수 있는지 체크
    for comb in permutations(dist, friends):
        if is_possible_work(interval, comb):
            return True
    return False


def solution(n, weak, dist):
    if len(weak) == 1:
        return 1
    interval = [weak[i] - weak[i-1]
                for i in range(len(weak))]  # (-1 ~ 0, 0 ~ 1, ...)
    interval[0] += n

    for i in range(len(dist)):
        if check(interval, sorted(dist, reverse=True), i + 1):  # i+1 명이 점검 가능?
            return i + 1
    return -1


n = 200
weak = [0, 10, 50, 80, 120, 160]
dist = [1, 10, 5, 40, 30]

print(solution(n, weak, dist))
