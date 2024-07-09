for tc in range(int(input())):
    n, m = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    flag = False
    answer = None
    for i in range(n):
        for j in range(n - m + 1):
            tmp = ''.join(graph[i][j:j+m])
            if tmp == tmp[::-1]:
                answer = tmp
                flag = True
                break
        if flag:
            break
    graph = list(zip(*graph))
    for i in range(n):
        for j in range(n - m + 1):
            tmp = ''.join(graph[i][j:j+m])
            if tmp == tmp[::-1]:
                answer = tmp
                flag = True
                break
        if flag:
            break
    print(f'#{tc + 1} {answer}')
