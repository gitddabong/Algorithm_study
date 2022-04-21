
def makeDirection(dir1, dir2):
  if dir1 == "E":
    if dir2 == "N":
      return "left"
    elif dir2 == "S":
      return "right"

  elif dir1 == "S":
    if dir2 == "E":
      return "left"
    elif dir2 == "W":
      return "right"

  elif dir1 == "W":
    if dir2 == "S":
      return "left"
    elif dir2 == "N":
      return "right"
  
  else:
    if dir2 == "W":
      return "left"
    elif dir2 == "E":
      return "right"

# path = "EEESEEEEEENNNN"
path = "SSSSSSWWWNNNNNN"

answer = []

dists = []
temp = ''
cnt = 0
for char in path:
  if not temp:
    temp = char
    cnt += 1
  elif temp == char:
    cnt += 1
  else:
    dists.append(cnt)
    temp = char
    cnt += 1


cur_way = 0
warning_flag = False
for i, char in enumerate(path):
  if dists[cur_way] - i <= 5 and not warning_flag:
    next_dir = path[dists[cur_way]]

    answer.append((i, (dists[cur_way] - i)*100 , makeDirection(char, next_dir)))
    warning_flag = True

  if dists[cur_way]-1 == i:
    cur_way += 1
    warning_flag = False

  elif dists[cur_way] - i > 5:
    warning_flag = False

  if cur_way == len(dists):
    break
  

print(answer)