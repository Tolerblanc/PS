import sys
input = sys.stdin.readline

n, b, a = map(int, input().split())
presents = sorted(map(lambda x: int(x) // 2, input().split()))

cnt = prefix = left = 0
for present in presents:
    if a:
        a -= 1
        if prefix + present > b:
            break
        cnt += 1
        prefix += present
    else:
        if prefix + presents[left] + present > b:
            break
        prefix += presents[left] + present
        left += 1
        cnt += 1
print(cnt)
