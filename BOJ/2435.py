import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temps = list(map(int, input().split()))
prefix = [0]
for temp in temps:
    prefix.append(prefix[-1] + temp)

answer = -4242
for right in range(n - k + 1):
    answer = max(answer, prefix[right + k] - prefix[right])
print(answer)
