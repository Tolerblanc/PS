import sys
input = sys.stdin.readline

dic = {}
n = int(input())
for _ in range(n):
    word = input().strip()
    for i, w in enumerate(word):
        dic[w] = dic.get(w, 0) + (10 ** (len(word) - i - 1))

lst = sorted(dic.items(), key=lambda x: -x[1])
num = 9
answer = 0
for k, v in lst:
    answer += num * v
    num -= 1
print(answer)
