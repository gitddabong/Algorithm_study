from collections import deque
import sys

def bfs():
  visited = [[float('inf')] * m for _ in range(n)]
  visited[0][0] = 1
  q = deque()
  q.append([0, 0])
  while q:
    x, y = q.popleft()
    cost = visited[x][y]
    if n-1 == x and m-1 == y:
      break
    
    for i in range(4):
      n_x = x + dx[i]
      n_y = y + dy[i]
      if (0 <= n_x < n and 0 <= n_y < m) and graph[n_x][n_y] == "1" and visited[n_x][n_y] == float('inf'):
        visited[n_x][n_y] = min(visited[n_x][n_y], cost + 1)
        q.append([n_x, n_y])

  return visited

if __name__ == "__main__":
  input = sys.stdin.readline
  n, m = map(int, input().split())
  graph = []
  for _ in range(n):
    graph.append(list(input().rstrip()))
  
  dx = [-1, 1, 0, 0]
  dy = [0 ,0, -1, 1]

  result = bfs()
  print(result[-1][-1])

