import sys
input = sys.stdin.readline

'''
N명이 M개의 1인승 놀이 기구를 기다림
각 놀이기구는 운행 시간이 정해져있음
빈 놀이기구 중 더 작은 번호가 적혀있는 놀이기구를 먼저 탑승
마지막 아이가 타게되는 놀이기구 번호?

파라메트릭 돌리면 lgN이고, M개 다 보긴 해야되니까 MlgN
파라메트릭으로 탐색 범위 좁힌 후 
주어진 배열 돌면서 마지막 번호 찾기
'''
n, m = map(int, input().split())
rides = list(map(int, input().split()))
if n <= m:
    print(n)
    exit()

right = 2_000_000_001 * 300_001
left = 0


def simulate(time):
    ridden = 0
    for ride in rides:
        ridden += time // ride + 1
    return ridden


while left <= right:
    mid = (left + right) // 2
    if simulate(mid - 1) < n <= simulate(mid):
        break
    if simulate(mid) >= n:
        right = mid - 1
    else:
        left = mid + 1


# 마지막 사람이 탑승한 번호 찾기
ridden = simulate(mid - 1)
for idx, ride in enumerate(rides):
    if mid % ride == 0:
        ridden += 1
        if ridden == n:
            break
print(idx + 1)
