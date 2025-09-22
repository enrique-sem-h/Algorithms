from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left, root.right)
    
root = TreeNode(1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(2, TreeNode(4), TreeNode(3))
)

print(Solution().isSymmetric(root))
