import sys

input = sys.stdin.readline

nums = ['1', '2', '3']
n = int(input())
length = 1
complete = False

def check(lst):
    if len(lst) <= 1:
        return False
    for i in range(2, len(lst) + 1, 2):
        for j in range(0, len(lst) - i + 1):
            token1 = lst[j : j + i//2]
            token2 = lst[j + i//2 : j + i]
            if token1 == token2:
                return True
    return False
            

def search(curr, cnt):
    global complete, length
    if complete:
        return
    if check(curr):
        return
    if cnt == n:
        print(''.join(curr))
        complete = True
        return
    for i in range(3):
        curr.append(nums[i])
        search(curr, cnt + 1)
        curr.pop()

answer = ['1']
search(answer, 1)