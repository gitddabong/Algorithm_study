# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.val = 0
        
        def order(root):
            if root is None:
                return
            
            order(root.right)
            self.val += root.val
            root.val = self.val
            order(root.left)
            
        order(root)
        return root
        
        
#         def order(root, weight = 0):
#             if root is None:
#                 return 0
            
#             right = order(root.right, weight)
#             weight = right + root.val
#             root.val = weight
#             left = order(root.left, weight)
            
#             return max(left, right)
            
#         order(root)
#         return root