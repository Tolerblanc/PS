import sys
input = sys.stdin.readline

n = int(input())
costs = list(map(int, input().split())) + [0, 0]
answer = 0


def check_3seq(idx):
    global answer
    b = min(costs[i], costs[i + 1], costs[i + 2])
    answer += 7 * b
    costs[idx] -= b
    costs[idx + 1] -= b
    costs[idx + 2] -= b


def check_2seq(idx):
    global answer
    a = min(costs[idx], costs[idx + 1] - costs[idx + 2]
            if costs[idx + 1] > costs[idx + 2] else costs[idx + 1])
    answer += 5 * a
    costs[idx] -= a
    costs[idx + 1] -= a


for i in range(n):
    if costs[i + 1] > costs[i + 2]:
        check_2seq(i)
        check_3seq(i)
    else:
        check_3seq(i)
        check_2seq(i)
    answer += 3 * costs[i]

print(answer)
