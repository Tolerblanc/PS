from collections import defaultdict, deque


def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1] * (n + 1)
    dist[destination] = 0
    q = deque([(destination, 0)])
    while q:
        prev, cost = q.popleft()
        for curr in graph[prev]:
            if dist[curr] == -1 or dist[curr] > cost + 1:
                dist[curr] = cost + 1
                q.append((curr, cost + 1))

    return [dist[i] for i in sources]
