import sys
input = sys.stdin.readline

n = int(input())

def checker(string):
    
    for s in string:
        if s in check:
            return 0
        check.add(s)
    else:
        return 1


answer = 0
for _ in range(n):
    answer += checker(input().rstrip())
print(answer)