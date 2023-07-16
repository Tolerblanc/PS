import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
cities = []
chickens = []
for r in range(n):
    inp = list(map(int, input().split()))
    for c in range(n):
        if inp[c] == 1:
            cities.append((r, c))
        if inp[c] == 2:
            chickens.append((r, c))

def get_chicken_dist(home, chickens):
    dist = 5000
    for chicken in chickens:
        dist = min(dist, abs(home[0] - chicken[0]) + abs(home[1] - chicken[1]))
    return dist
    
combination_chicken = list(combinations(chickens, m))
result = [5000] * len(combination_chicken)
for i, cc in enumerate(combination_chicken):
    temp = 0
    for home in cities:
        temp += get_chicken_dist(home, cc)
    result[i] = temp
print(min(result))