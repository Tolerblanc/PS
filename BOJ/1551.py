import sys
input = sys.stdin.readline

n, k = map(int, input().split())
seq = list(map(int, input().rstrip().split(',')))

for _ in range(k):
    seq = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
print(*seq, sep=',')
