def selfNum(n):
    return n + sum([int(num) for num in str(n)])


hasConstructor = [False] * 100001

for i in range(1, 10001):
    hasConstructor[selfNum(i)] = True
    if not hasConstructor[i]:
        print(i)