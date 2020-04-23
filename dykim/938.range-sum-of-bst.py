# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.rangeSum(root, L, R)
    
    
    def rangeSum(self, node: TreeNode, L: int, R: int) -> int:
        if node == None:
            return 0
        
        if node.val < L:
            return self.rangeSum(node.right, L, R)
        if node.val > R:
            return self.rangeSum(node.left, L, R)
        
        
        return node.val + self.rangeSum(node.left, L, R) + self.rangeSum(node.right, L, R)
