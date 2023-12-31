def dfs(n, trees):
    visited = [False] * (n + 1)
    stack = [1]
    visited[1] = True
    while stack:
        prev = stack.pop()
        for curr in trees[prev]:
            if not visited[curr]:
                visited[curr] = True
                stack.append(curr)
    return abs(sum(visited) * 2 - n)
        

def solution(n, wires):
    answer = 100001
    trees = [[] for _ in range(n + 1)]
    for wire in wires:
        trees[wire[0]].append(wire[1])
        trees[wire[1]].append(wire[0])
    
    for wire in wires:
        trees[wire[0]].remove(wire[1])
        trees[wire[1]].remove(wire[0])
        answer = min(answer, dfs(n, trees))
        trees[wire[0]].append(wire[1])
        trees[wire[1]].append(wire[0])
        
    return answer