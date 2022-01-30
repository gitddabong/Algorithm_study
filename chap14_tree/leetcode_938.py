# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum = 0
        
        def preorder(root):
            if root is None:
                return
            
            preorder(root.left)
            
            if low <= root.val <= high:
                self.sum += root.val
            
            preorder(root.right)
            
        preorder(root)
        return self.sum