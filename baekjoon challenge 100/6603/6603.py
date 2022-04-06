import sys
from collections import deque

def dfs(result, index = 0, depth = 0):
  if depth == 6:
    print(*result, sep = ' ')
    return

  for i in range(index, length):
    result.append(nums[i])
    dfs(result, i+1, depth+1)
    result.pop()

if __name__ == "__main__":
  input = sys.stdin.readline

  while True:
    nums = list(map(int, input().split()))
    length = nums.pop(0)
    if length == 0:
      break

    result = deque()

    dfs(result)
    print()