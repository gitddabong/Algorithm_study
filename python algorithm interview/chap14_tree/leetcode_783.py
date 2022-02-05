# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 이진 탐색 트리에서 루트와 가장 근사한 값을 가지는 노드는 총 2개.
        # 왼쪽 서브트리에서 가장 오른쪽의 노드, 오른쪽 서브트리에서 가장 왼쪽의 노드다.
        # 모든 노드를 순회하며 각 노드와 이 둘만 비교해서 차이값의 최솟값을 저장
        
        
        self.result = float('inf')
        
        def search_left(root):
            curr = root.left
            while curr.right:
                curr = curr.right
            
            return curr.val
        
        
        def search_right(root):
            curr = root.right
            while curr.left:
                curr = curr.left
                
            return curr.val
            

        def dfs(root):
            if root is None:
                return
            
            max_left = 1000000     # 딱히 의미 없는 엄청 큰 값
            min_right = 1000000
            if root.left:
                max_left = search_left(root)
            
            if root.right:
                min_right = search_right(root)
            
            self.result = min(self.result, abs(root.val - max_left), abs(min_right - root.val))
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return self.result
        
        
        
        
#         self.result = float('inf')
#         self.min_val = float('inf')
        
#         def dfs(root, parent_val = 1000):
#             if not root:
#                 return
            
#             temp = abs(parent_val - root.val)
#             self.result = min(self.result, temp)
            
#             dfs(root.left, root.val)
#             dfs(root.right, root.val)
            
#         dfs(root)
#         return self.result
            