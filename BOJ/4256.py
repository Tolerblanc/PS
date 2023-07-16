import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(3000)

def postorder(in_left, in_right, pre_left, pre_right):
    global n, inorder, preorder, idx, answer
    if in_left > in_right or pre_left > pre_right:
        return
    if in_left < 0 or in_right >= n or pre_left < 0 or pre_right >= n:
        return
    root_idx = idx[preorder[pre_left]]
    sub = root_idx - in_left
    postorder(in_left, root_idx - 1, pre_left + 1, pre_left + sub)
    postorder(root_idx + 1, in_right, pre_left + sub + 1, pre_right)
    answer.append(inorder[root_idx])

tc = int(input().rstrip())
for _ in range(tc):
    n = int(input().rstrip())
    preorder = list(map(int, input().rstrip().split()))
    inorder = list(map(int, input().rstrip().split()))
    idx = [0] * (n + 1)
    for i in range(1, n + 1):
        idx[inorder[i - 1]] = i - 1
    answer = []
    postorder(0, n - 1, 0, n - 1)
    print(*answer)