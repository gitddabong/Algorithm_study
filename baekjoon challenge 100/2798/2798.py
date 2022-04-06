import sys
input = sys.stdin.readline

n, target = map(int, input().split())
nums = list(map(int,input().split()))

result = 0
def dfs(index = 0, total = 0, depth = 0):
  global result
  if depth == 3:
    if not total > target:
      result = max(result, total)
    return

  for i in range(index, n-2+depth):
    dfs(i + 1, total + nums[i], depth + 1)

dfs()
print(result)


# 실패. 모든 케이스를 다 확인할 수 없음
# nums.sort()

# left = 0
# right = n-1

# result = 0
# isBig = False
# while left+1 <= right:
#   left_val = nums[left]
#   right_val = nums[right]

#   for mid in range(left+1, right):
#     mid_val = nums[mid]
#     total = left_val + mid_val + right_val
#     if total <= target:
#       result = max(result, total)
#     elif total > target:
#       isBig = True
#       break
  
#   if isBig:
#     isBig = False
#     right -= 1
#   else:
#     left += 1

# print(result)