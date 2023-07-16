import sys

#sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input().rstrip())
suffix = list(map(int, input().rstrip().split()))
for _ in range(n - 1):
    inp = list(map(int, input().rstrip().split()))
    inp[0] += min(suffix[1], suffix[2])
    inp[1] += min(suffix[0], suffix[2])
    inp[2] += min(suffix[0], suffix[1])
    suffix[0], suffix[1], suffix[2] = inp[0], inp[1], inp[2]

print(min(suffix))