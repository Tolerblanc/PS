import sys
input = sys.stdin.readline


def is_group_sentence(string):
    checker = set()
    i = 0
    while i < len(string):
        curr = string[i]
        if curr in checker:
            return False
        checker.add(curr)
        i += 1
        while i < len(string) and curr == string[i]:
            i += 1
    return True


n = int(input())
answer = 0
for _ in range(n):
    answer += is_group_sentence(input().rstrip())
print(answer)
