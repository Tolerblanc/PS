import sys


class Solution:
    answer = 0
    is_odd = [0] * 10

    def isPseudoPalindromic(self) -> bool:
        # 하나만 홀수이거나
        # 전부 짝수이면 유사 팰린드롬
        return sum(self.is_odd) <= 1

    def dfs(self, curr: Optional[TreeNode], depth) -> None:
        self.is_odd[curr.val] ^= 1
        if curr.left:
            self.dfs(curr.left, depth + 1)
        if curr.right:
            self.dfs(curr.right, depth + 1)
        if not curr.left and not curr.right and self.isPseudoPalindromic():
            self.answer += 1
        self.is_odd[curr.val] ^= 1

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        sys.setrecursionlimit(100001)
        self.dfs(root, 1)
        return self.answer
