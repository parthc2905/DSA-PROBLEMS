# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        x = self.leafnodes(root1,[])
        y = self.leafnodes(root2,[])
        if x==y:
            return True
        return False
    
    def leafnodes(self, node, leaf):
        if not node:
            return 
        if not node.left and not node.right:
            leaf.append(node.val)
        self.leafnodes(node.left, leaf)
        self.leafnodes(node.right, leaf)

        return leaf
