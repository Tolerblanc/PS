import sys
input = sys.stdin.readline

while True:
    seq = list(map(int, input().split()))
    if seq[0] == -1:
        break
    check = set(seq[:-1])
    answer = 0
    for num in seq[:-1]:
        if num * 2 in check:
            answer += 1
    print(answer)
