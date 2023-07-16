import sys

input = sys.stdin.readline

n = int(input())
net = [True for _ in range(n + 1)]
net[0] = net[1] = False
for i in range(2, n + 1):
    if net[i] == True:
        j = 2
        while i * j <= n:
            net[i * j] = False
            j += 1
primes = [i for i, x in enumerate(net) if x]

p1 = p2 = 0
limit = len(primes)
answer = 0
while p1 < limit and p2 + 1 <= limit:
    prefix = sum(primes[p1:p2 + 1])
    if prefix == n:
        answer += 1
        p2 += 1
    elif prefix < n:
        p2 += 1
    else:
        p1 += 1
print(answer)