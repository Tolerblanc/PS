def diff(string1, string2):
    diff = 0
    for s1, s2 in zip(string1, string2):
        diff += 1 if s1 != s2 else 0
    return diff


def solution(begin, target, words):
    visited = [False] * len(words)
    answer = 100

    def dfs(words, curr, target, depth, visited):
        nonlocal answer
        if curr == target:
            answer = min(answer, depth)
        for idx, word in enumerate(words):
            if not visited[idx] and diff(curr, word) == 1:
                visited[idx] = True
                dfs(words, word, target, depth + 1, visited)
                visited[idx] = False

    dfs(words, begin, target, 0, visited)
    return answer if answer != 100 else 0
