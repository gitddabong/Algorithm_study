# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.longest = 0
        
        def dfs(root):
            if not root:
                return -1   # 맨 아래지점 카운트를 -1로 시작해서 노드를 한 칸씩 올라갈 때마다 1씩 추가
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.longest = max(self.longest, left + right + 2)      # 2를 더해주는 이유는 왼쪽 노드와 오른쪽 노드 양쪽을 세어주기 위함. 노드 초기값을 -1로 잡아놓았으므로 이렇게 해도 예외처리가 가능.
            return max(left, right) + 1     # return값으로 넘겨주는 값은 지금까지 left와 right 중 가장 길었던 길이.
            
        dfs(root)
        return self.longest
        
        
        
        
        
        
        
        
        
        
        
        
        # 이건 교재 코드
#         self.longest = 0
        
#         def dfs(node):
#             if not node:
#                 return -1
            
#             # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
#             left = dfs(node.left)
#             right = dfs(node.right)
            
#             # 가장 긴 경로
#             self.longest = max(self.longest, left + right + 2)
#             # 상태값
#             return max(left, right) + 1

#         dfs(root)
#         return self.longest
        
        
#         # 실패작. root를 거치지 않고도 최대 거리가 나올 수 있다
        
#         self.height = 0
        
#         def get_depth(root, depth):
#             if root == None:
#                 self.height = max(self.height, depth - 1)
#                 return
            
#             print(root.val)
#             get_depth(root.left, depth + 1)
#             get_depth(root.right, depth + 1)
                 
#         get_depth(root.left, 1)
#         left_height = self.height
        
#         self.height = 0
        
#         get_depth(root.right, 1)
#         right_height = self.height
        
#         return left_height + right_height