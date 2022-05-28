def dfs(x, y, field, visited, cnt = 1):
  visited[x][y] = True
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  for i in range(4):
    n_x = x + dx[i]
    n_y = y + dy[i]
    if 0 <= n_x < len(field) and 0 <= n_y < len(field[0]):
      if not visited[n_x][n_y] and field[n_x][n_y] == 1:
        cnt = dfs(n_x, n_y, field, visited, cnt + 1)

  return cnt

def solution(v):
  answer = 0
  max_val = 0
  visited = [[False] * len(v[0]) for _ in range(len(v))]

  for i in range(len(v)):
    for j in range(len(v[0])):
      if not visited[i][j] and v[i][j] == 1:
        max_val = max(max_val, dfs(i, j, v, visited))
        answer += 1
        
  return answer, max_val

print(solution(
  [
    [1,1,0,1,1],
    [0,1,1,0,0],
    [0,0,0,0,0],
    [1,1,0,1,1],
    [1,0,1,1,1],
    [1,0,1,1,1]
  ]
))