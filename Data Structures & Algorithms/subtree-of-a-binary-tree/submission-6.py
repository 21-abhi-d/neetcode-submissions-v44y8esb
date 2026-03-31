# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        
        def isSameTree(r, s):
            if not r and not s:
                return True
            if (not r or not s) or (r.val != s.val):
                return False

            left = isSameTree(r.left, s.left)
            right = isSameTree(r.right, s.right)

            return left and right
        
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)