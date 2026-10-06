# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.node = 0

        def dfs_in_order(root):
            if not root: return

            left = dfs_in_order(root.left)
            if self.count == 1: self.node = root.val
            self.count -= 1
            if self.count > 0: 
                right = dfs_in_order(root.right)
            return
        dfs_in_order(root)
        return self.node

