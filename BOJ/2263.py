import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
answer = []

def preorder(in_left, in_right, post_left, post_right):
    if in_left > in_right or post_left > post_right:
        return
    if in_left < 0 or in_right >= n or post_left < 0 or post_right >= n:
        return
    root_idx = inorder.index(postorder[post_right])
    answer.append(inorder[root_idx])
    sub = root_idx - in_left
    preorder(in_left, root_idx - 1, post_left, post_left + sub - 1)
    preorder(root_idx + 1, in_right, post_left + sub , post_right - 1)
    
preorder(0, n - 1, 0, n - 1)
print(*answer)