import sys
input = sys.stdin.readline


def calculate_density(d1, d2, chi):
    d1, d2 = max(d1, d2), min(d1, d2)
    m1_ratio = chi / 100
    m2_ratio = (100 - chi) / 100
    return 1 / (m1_ratio / d1 + m2_ratio / d2)


d1, d2, chi = map(int, input().split())
result = calculate_density(d1, d2, chi)
print(f"{result:.14f}")
