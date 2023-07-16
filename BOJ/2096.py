import sys

input = sys.stdin.readline

n = int(input())
maxlst = [0, 0, 0]
minlst = [0, 0, 0]

def copy_list(src):
    temp = [0, 0, 0]
    for i in range(3):
        temp[i] = src[i]
    return temp

for _ in range(n):
    a, b, c = map(int, input().split())
    temp = copy_list(maxlst)
    maxlst[0] = a + max(temp[0], temp[1])
    maxlst[1] = b + max(temp[0], temp[1], temp[2])
    maxlst[2] = c + max(temp[1], temp[2])
    temp = copy_list(minlst)
    minlst[0] = a + min(temp[0], temp[1])
    minlst[1] = b + min(temp[0], temp[1], temp[2])
    minlst[2] = c + min(temp[1], temp[2])
    
print(max(maxlst), min(minlst))