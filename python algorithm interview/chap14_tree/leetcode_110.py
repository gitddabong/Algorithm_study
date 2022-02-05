# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
                
        self.flag = True
        
        def dfs(root):
            if not self.flag:   # 플래그가 false가 되면 결과 나왔으니 더 이상 연산해줄 필요 없음.
                return -1
                
            if root is None:
                return 0

            left = dfs(root.left)       # 왼쪽 자식노드 높이
            right = dfs(root.right)     # 오른쪽 자식 노드 높이

            if abs(left - right) > 1:   # 차이가 2이상 나면 플래그 저장
                self.flag = False

            return max(left, right) + 1 # 왼쪽 오른쪽 중 가장 높은 높이에 +1해서 다음 재귀에 반환
        
        dfs(root)
        return self.flag
        
        
        
#         self.height = 0
        
#         def getDepth(root, depth = 1):
#             if root is None:
#                 self.height = max(self.height, depth - 1)
#                 return
            
#             getDepth(root.left, depth + 1)
#             getDepth(root.right, depth + 1)
            
        
#         if root:
#             getDepth(root.left)
#             left = self.height
#             self.height = 0
            
#             getDepth(root.right)
#             right = self.height
            
#             result = abs(left- right)
            
#             if result == 1 or result == 0:
#                 return True
#             else:
#                 return False
        
#         else:
#             return True
            
        
        
        