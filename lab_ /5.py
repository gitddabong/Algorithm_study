def dfs(nums, visited, result, cur = 0, cnt = 0):
  if cur == len(nums)-1:
    result.append(cnt)
    return

  n_cur1 = cur - nums[cur]
  n_cur2 = cur + nums[cur]

  if 0 <= n_cur1 and not visited[n_cur1]:
    visited[n_cur1] = True
    dfs(nums, visited, result, n_cur1, cnt + 1)
  if n_cur2 < len(nums) and not visited[n_cur2]:
    visited[n_cur2] = True
    dfs(nums, visited, result, n_cur2, cnt + 1)

  return

def solution(nums):
  result = []
  
  visited = [False] * len(nums)
  visited[0] = True
  dfs(nums, visited, result)

  if result:
    return min(result)
  else:
    return -1

nums = [4,1,2,3,1,0,5]
print(solution(nums))