import sys
input = sys.stdin.readline


def check(lst):
    if len(set(lst)) <= 2:
        return True
    lst.sort()
    if lst[0] == lst[1] and lst[2] == lst[3]:
        return True
    for _ in range(4):
        curr = lst.pop(0)
        tmp = sorted(lst)
        if tmp[0][1] == tmp[1][1] == tmp[2][1]:
            if int(tmp[2][0]) == int(tmp[1][0]) + 1 == int(tmp[0][0]) + 2:
                return True
        lst.append(curr)
    return False


for _ in range(int(input())):
    print(":)" if check(input().split()) else ":(")
