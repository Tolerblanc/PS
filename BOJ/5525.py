import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

# p_n 에는 p_k 가 n-k+1 개 들어있음
subsq = []

i = 0
while (i < m - 1):
    if (s[i] == 'I'):
        i += 1
        k = 0
        while (s[i:i+2] == "OI"):
            k += 1
            i += 2
        if (k > 0):
            subsq.append(k)
    else:
        i += 1

ans = 0
print(subsq)
for sq in subsq:
    if (sq >= n):
        ans += sq - n + 1

print(ans)
