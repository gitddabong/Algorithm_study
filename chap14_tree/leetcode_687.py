# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # 아래부터 시작해서 left와 right값을 같은 수가 나올 때마다 +1 해주는 방식.
        
        self.longest = 0
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)       # 아래 노드들에서 가장 높은 카운트 가져오기
            right = dfs(root.right)
            
            # 왼쪽 자식이 값이 같으면 +1, 아닌 경우는 길이 끊겨버리므로 값을 0으로 초기화
            if root.left and root.left.val == root.val:
                left += 1
            else:
                left = 0
                
            # 오른쪽도 마찬가지.
            if root.right and root.right.val == root.val:
                right += 1
            else:
                right = 0
                
            # 전역 변수에 결과값 저장
            self.longest = max(self.longest, left + right)
            return max(left, right)     # 지금까지 가장 높았던 수 저장
                
        
        dfs(root)
        return self.longest
