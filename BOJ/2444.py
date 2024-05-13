n = int(input())
l = [' ' * (n - 1 - i) + '*' * (2 * i + 1) for i in range(n)]
print(*l, *l[-2::-1], sep='\n')
