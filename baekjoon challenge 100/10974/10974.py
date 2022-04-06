import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [x for x in range(1, n + 1)]
visited = [0] * n
result = deque()

def dfs(list, depth = 0):
  if depth == n:
    print(*list, sep = ' ')
    return

  for i in range(n):
    if visited[i] == 0:
      list.append(arr[i])
      visited[i] = 1

      dfs(list, depth + 1)
      
      visited[i] = 0
      list.pop()

dfs(result)