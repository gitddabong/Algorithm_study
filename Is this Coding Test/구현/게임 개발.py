from sys import setrecursionlimit


setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
x, y, loc = map(int ,input().split())
field = []
for _ in range(n):
  field.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

def dfs(x, y, loc):
  global result, field

  for i in range(1, 5):
    n_loc = (loc - i) % 4
    n_x = x + dx[n_loc]
    n_y = y + dy[n_loc]

    if field[n_x][n_y] == 0:
      result += 1
      field[n_x][n_y] = 1
      dfs(n_x, n_y, n_loc)
  
  return

dfs(x, y, loc)
print(result)