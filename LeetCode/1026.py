class Solution:
    def calculateAllAncestorDiff(self, root):
        result = 0
        leftNodes = []
        rightNodes = []
        if root.left:
            localMax, leftNode = self.calculateAllAncestorDiff(root.left)
            result = max(result, localMax)
            leftNodes += leftNode
        if root.right:
            localMax, rightNode = self.calculateAllAncestorDiff(root.right)
            result = max(result, localMax)
            rightNodes += rightNode
        for node in leftNodes + rightNodes:
            result = max(result, abs(root.val - node))
        return result, leftNodes + rightNodes + [root.val]

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        answer, _ = self.calculateAllAncestorDiff(root)
        return answer
