import sys

def makeNewNum(num):
    return num%10*10 + (num//10 + num%10)%10

def getCycle(num):
    target = num
    count = 0
    while True:
        target = makeNewNum(target)
        count += 1
        if target != num:
            continue
        break
    return count

target = int(sys.stdin.readline())
print(getCycle(target))