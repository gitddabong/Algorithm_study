data = input()
x = int(data[1]) - 1
y = ord(data[0]) - 97

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

cnt = 0
for i in range(8):
  next_x = x + dx[i]
  next_y = y + dy[i]
  if 0 <= next_x <= 7 and 0 <= next_y <= 8:
    cnt += 1

print(cnt)
