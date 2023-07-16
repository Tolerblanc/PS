import sys

input = sys.stdin.readline

form = input()
lst = form.split('-')

result = 0
for i in range(len(lst)):
    if '+' in lst[i]:
        temp = list(map(int, lst[i].split('+')))
        lst[i] = sum(temp)
    else:
        lst[i] = int(lst[i])
    if i == 0:
        result += lst[i]
    else:
        result -= lst[i]

print(result)