import sys
input = sys.stdin.readline

l, k, c = map(int, input().split())
logs = sorted(set(map(int, input().split())))
logs.append(l)
parts = [logs[0]]
for i in range(1, len(logs)):
    parts.append(logs[i] - logs[i - 1])
first_cut = 0


def check(mid):
    global first_cut
    cut_cnt, suffix = 0, 0
    for part in reversed(parts):
        if part > mid:
            return False
        suffix += part
        if suffix > mid:
            suffix = part
            cut_cnt += 1
    if cut_cnt > c:
        return False
    first_cut = suffix if cut_cnt == c else logs[0]
    return True


left, right = 0, l
length = 1000000001
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
        length = min(length, mid)
    else:
        left = mid + 1

print(length, first_cut)
