n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(input()))

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  global visited

  for i in range(4):
    n_x = x + dx[i]
    n_y = y + dy[i]

    if 0 <= n_x < n and 0 <= n_y < m:
      if board[n_x][n_y] == '0' and visited[n_x][n_y] == False:
        visited[n_x][n_y] = True
        dfs(n_x, n_y)

result = 0
for i in range(n):
  for j in range(m):
    if board[i][j] == '0' and visited[i][j] == False:
      dfs(i, j)
      result += 1

print(result)