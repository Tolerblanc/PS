import sys
input = sys.stdin.readline

for _ in range(int(input())):
    nums = [num for num in map(int, input().split()) if num % 2 == 0]
    print(sum(nums), min(nums))