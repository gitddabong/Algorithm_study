# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)      # 두 트리가 모두 가지고 있는 노드는 새로 만들어서 연결
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            
            return node
        
        else:
            # 양쪽 중 하나만 갖고 있는 노드는 그 노드를 가져와서 결과물 트리에 연결.
            # 이렇게 하면 어느 쪽도 노드가 없는 경우도 처리 가능. 어차피 둘 중 아무거나 리턴해줘도 None이니까.
            return root1 or root2   

            
            
        
        # 실패작
#         curr = result = TreeNode(0)
        
#         def makeNewTree(root1, root2, new_tree):
#             if not root1 and not root2:
#                 return
            
#             new_node = TreeNode(0)
            
#             # 노드가 양쪽 모두 있는 경우
#             if root1 and root2:
#                 new_node.val = root1.val + root2.val
            
#             # 노드가 root1에만 있는 경우
#             elif root1 and not root2:
#                 new_node.val = root1.val
            
#             # 노드가 root2에만 있는 경우
#             elif not root1 and root2:
#                 new_node.val = root2.val
                
#             makeNewTree(root1.left, root2.left, new_tree.left)
#             makeNewTree(root1.right, root2.right, new_tree.right)
            
            
#         makeNewTree(root1, root2, result.left)
        
#         return result.left