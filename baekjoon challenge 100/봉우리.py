n = int(input())
field = []
field.append([0] * (n+2))
for _ in range(n):
  temp_list = list(map(int, input().split()))
  temp_list.insert(0, 0)
  temp_list.append(0)
  field.append(temp_list)
field.append([0] * (n+2))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def searchTop():
  result = 0
  for x in range(1, n+1):
    for y in range(1, n+1):
      cnt = 0
      for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        if field[x][y] > field[n_x][n_y]:
          cnt += 1
      if cnt == 4:
        result += 1
  return result
  
print(searchTop())