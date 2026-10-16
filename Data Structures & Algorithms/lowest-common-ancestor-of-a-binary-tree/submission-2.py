# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root):
            if not root or root is p or root is q: return root

            left = lca(root.left)
            right = lca(root.right)
            
            if left and right: return root

            return left or right
        
        return lca(root)
