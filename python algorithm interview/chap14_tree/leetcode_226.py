# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def dfs(root):
            if root.left == None and root.right == None:
                return
            
            temp = root.left
            root.left = root.right
            root.right = temp
            
            # 한 쪽 노드만 존재하는 경우를 대비한 if문 추가
            if root.left:
                dfs(root.left)
            
            if root.right:
                dfs(root.right)
        
        if root:
            dfs(root)

        return root