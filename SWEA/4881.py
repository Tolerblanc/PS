def backtracking(graph, depth, value, visited):
    global answer
    if value > answer:
        return
    if depth == len(graph):
        answer = min(answer, value)
        return
    for idx, n in enumerate(graph[depth]):
        if not visited[idx]:
            visited[idx] = True
            backtracking(graph, depth + 1, value + n, visited)
            visited[idx] = False


for tc in range(int(input())):
    graph = [list(map(int, input().split())) for _ in range(int(input()))]
    answer = 10001
    visited = [False] * len(graph)
    backtracking(graph, 0, 0, visited)
    print(f'#{tc + 1} {answer}')
