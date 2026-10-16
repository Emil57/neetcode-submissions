# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.node = None

        def inorder(root):
            if not root: return

            left = inorder(root.left)
            if self.count == 1: 
                self.node = root.val
            self.count-=1
            right = inorder(root.right)
        inorder(root)
        return self.node
            

