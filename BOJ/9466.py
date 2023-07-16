import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

tc = int(input().rstrip())

def check_team(graph, visited, start):
    route = []
    curr = start
    result = 0
    while True:
        if visited[curr] >= 0: #already checked
            while route:
                temp = route.pop()
                if visited[temp] != 0:
                    visited[temp] = 0
                    result += 1
            break
        elif visited[curr] == -1: #visit first
            route.append(curr)
            visited[curr] = -2
            curr = graph[curr]
        elif visited[curr] == -2: #cycle detected
            if graph[curr] == start: #perfect cycle
                while route:
                    visited[route.pop()] = 1
            else: #imperfect cycle
                flag = True
                while route:
                    temp = route.pop()  
                    if flag:
                        visited[temp] = 1
                    else:
                        visited[temp] = 0
                        result += 1
                    if temp == curr:
                        flag = False
            break
    return result
        
for _ in range(tc):
    answer = 0
    n = int(input().rstrip())
    stus = [0] + list(map(int, input().rstrip().split()))
    visited = [-1] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] == -1:
            answer += check_team(stus, visited, i)
    print(answer)