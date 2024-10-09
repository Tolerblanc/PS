import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = input().rstrip()

stack = [nums[0]]
for num in nums[1:]:
    while k > 0 and stack and stack[-1] < num:
        stack.pop()
        k -= 1
    stack.append(num)

while k and stack:
    k -= 1
    stack.pop()

print(*stack, sep='')
