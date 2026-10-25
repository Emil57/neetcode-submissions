# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return 0, True

            l_height, l_balanced = dfs(node.left)
            r_height, r_balanced = dfs(node.right)
            height = 1 + max(l_height, r_height)
            balanced = l_balanced and r_balanced and abs(r_height - l_height) <= 1
            return height, balanced
        return dfs(root)[1]
        # Time O(n)
        # Time O(h)