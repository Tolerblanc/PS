def print_star_triangle_outline(n):
    for i in range(1, n+1):
        if i == 1:
            print(' ' * (n - i) + '*')
        elif i == n:
            print('*' * (2*i - 1))
        else:
            print(' ' * (n - i) + '*' + ' ' * (2*i - 3) + '*')


n = int(input())
print_star_triangle_outline(n)
