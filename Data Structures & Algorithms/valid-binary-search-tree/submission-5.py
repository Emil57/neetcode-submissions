# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst(root, minn, maxx):
            if not root: return True

            if not (minn < root.val < maxx): return False

            left = bst(root.left, minn, root.val)

            right = bst(root.right, root.val, maxx)
            return left and right
        return bst(root,float('-inf'),float('inf'))




        

        