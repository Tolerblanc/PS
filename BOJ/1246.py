import sys
input = sys.stdin.readline

n, m = map(int, input().split())
consumers = []
for _ in range(m):
    consumers.append(int(input()))

consumers.sort(reverse=True)
price = 0
total = 0
for idx, consumer in enumerate(consumers):
    if idx + 1 > n:
        break
    if (idx + 1) * consumer > total:
        price = consumer
        total = (idx + 1) * price
print(price, total)
