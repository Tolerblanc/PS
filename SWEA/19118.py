from bisect import bisect_left
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    houses = list(map(int, input().split()))
    dp = [0]
    for house in houses:
        dest = bisect_left(dp, house)
        if dest == len(dp) and dp[-1] < house:
            dp.append(house)
        else:
            dp[dest] = house
    print(f'#{test_case} {len(houses) - len(dp) + 1}')