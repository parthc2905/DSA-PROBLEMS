# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.leftLeaves(root, False)
    
    def leftLeaves(self, node, isleft):
        if not node:
            return 0

        if not node.left and not node.right:
            return node.val if isleft else 0

        return self.leftLeaves(node.left, True) + self.leftLeaves(node.right, False)

