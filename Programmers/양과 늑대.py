left = [-1] * 20
right = [-1] * 20
visited = [False] * (1 << 17)
answer = 1


def flood_fill(bit_state, info):
    global answer
    if visited[bit_state]:
        return
    visited[bit_state] = True

    wolf = num = 0
    # 현재 상태에서 방문한 모든 노드에 대해
    for i in range(len(info)):
        if bit_state & (1 << i):
            wolf += info[i]
            num += 1

    if 2 * wolf >= num:
        return
    answer = max(answer, num - wolf)

    for i in range(len(info)):
        if not bit_state & (1 << i):
            continue
        if left[i] != -1:
            flood_fill(bit_state | (1 << left[i]), info)
        if right[i] != -1:
            flood_fill(bit_state | (1 << right[i]), info)


def solution(info, edges):
    for a, b in edges:
        if left[a] == -1:
            left[a] = b
        else:
            right[a] = b
    flood_fill(1, info)
    return answer
