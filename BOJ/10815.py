import sys
input = sys.stdin.readline

_ = input()
hand = set(map(int, input().split()))
_ = input()
pending = list(map(int, input().split()))
print(*[1 if p in hand else 0 for p in pending])
