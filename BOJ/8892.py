from itertools import permutations
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    words = [input().rstrip() for _ in range(int(input()))]
    for word in permutations(words, 2):
        check = ''.join(word)
        if check == check[::-1]:
            print(check)
            break
    else:
        print(0)
