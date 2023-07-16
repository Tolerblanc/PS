import sys
nums = []
numOfTarget = int(sys.stdin.readline())
for i in range(numOfTarget):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for num in nums:
    print(num)