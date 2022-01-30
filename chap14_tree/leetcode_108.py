# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 분할 정복 풀이법.
        # 첫 루트 노드를 정할 때 중간값으로 정해서 놓고
        # 그 다음 서브 트리를 만들 때도 그 리스트에서 중간값을 골라 루트 노드로 설정
        
        if not nums:
            return None
            
        mid = len(nums) // 2
        
        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return node
        
        # 분할 정복 없이 넣어주니 균형 이진 트리가 만들어지지 않는다
#         length = len(nums)
        
#         middle = 0      # 루트로 잡을 원소의 index
#         if length >= 2:
#             middle = length // 2
            
#         numbers = nums[:]
#         numbers.pop(middle)
        
#         root = TreeNode(nums[middle])
        
#         def insertNode(root, num):
#             if root is None:
#                 return TreeNode(num)
            
#             if root.val > num:
#                 root.left = insertNode(root.left, num)
#             elif root.val < num:
#                 root.right = insertNode(root.right, num)

#             return root     # 중복 수가 들어온 경우 삽입하지 않음
        
#         for num in numbers:
#             insertNode(root, num)
            
#         return root
        