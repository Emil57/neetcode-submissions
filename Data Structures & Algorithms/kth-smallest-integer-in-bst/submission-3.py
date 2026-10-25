# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.node = None
        self.count = k

        def dfs(node):
            if not node: return
            left = dfs(node.left)
            if self.count == 1: self.node = node.val
            self.count-=1
            right = dfs(node.right)
            return
        dfs(root)
        return self.node
        # Time O(n)
        # Space O(1)