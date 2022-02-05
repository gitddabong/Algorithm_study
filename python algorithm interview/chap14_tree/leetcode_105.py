# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        # 전위 순회로 알 수 있는 것은 트리(서브트리도 포함)의 루트
        # 중위 순회로 알 수 있는 것은 루트를 기준으로 어느 쪽이 왼쪽 서브트리이고 오른쪽 서브트리인지.
        # 책 코드
#         if inorder:
#             root_val = preorder.pop(0)
            
#             newNode = TreeNode(root_val)
#             root_idx = inorder.index(root_val)
            
#             newNode.left = self.buildTree(preorder, inorder[:root_idx])
#             newNode.right = self.buildTree(preorder, inorder[root_idx+1:])
            
#             return newNode
        

        # 직접 짠 코드        
        if preorder:
            root_val = preorder[0]
            
            newNode = TreeNode(root_val)
            root_idx = inorder.index(root_val)
            
            newNode.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
            newNode.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
            
            return newNode
        
        return None