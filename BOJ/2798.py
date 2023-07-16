import sys

numOfCards, maxOfSum = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
sums = []

for a in cards:
    for b in cards[cards.index(a):]:
        for c in cards[cards.index(b):]:
            if a+b+c <= maxOfSum :
                sums.append(a+b+c)

print(max(sums))