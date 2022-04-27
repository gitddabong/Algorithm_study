n = int(input())
locations = list(input().split())

x = 1
y = 1
for loc in locations:
  if loc == 'L':
    if y == 1:
      continue
    y -= 1

  elif loc == 'R':
    if y == n:
      continue
    y += 1

  elif loc == 'U':
    if x == 1:
      continue
    x -= 1

  else:
    if x == n:
      continue
    x += 1

print(x, y)