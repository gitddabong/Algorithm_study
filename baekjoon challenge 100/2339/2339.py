n = int(input())
field = []
for _ in range(n):
  field.append(list(input().split()))

# 불순물, 보석 개수 구하기
def checkcase(x1, x2, y1, y2):
  jewel = trash = 0
  for i in range(x1, x2+1):
    for j in range(y1, y2+1):
      if field[i][j] == '2':
        jewel += 1
      elif field[i][j] == '1':
        trash += 1
  
  return jewel, trash

def solution(x1, x2, y1, y2, arrow):
  jewel, trash = checkcase(x1, x2, y1, y2)
  if jewel == 1 and trash == 0:
    return 1
  if jewel == 0:
    return 0
  if jewel != trash + 1:
    return 0
  
  cnt = 0
  for i in range(x1, x2+1):
    for j in range(y1, y2+1):
      if field[i][j] == '1':
        if arrow == 1:
          if i < 1 or i >= x2:
            continue
  

  if trash == cnt:
    
  


  

