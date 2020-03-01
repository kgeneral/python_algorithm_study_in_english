# https://leetcode.com/explore/interview/card/microsoft/31/trees-and-graphs/153/
# elapsed time : around 10 min
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorder(root)
    
    def inorder(self, node):
        if node == None:
            return []
        
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)
