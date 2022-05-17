n = int(input())
field = []
for _ in range(n):
  field.append(list(input().split()))


cnt = 0
# x, y 넣으면 그 루트로 모두 가둘 수 있는 경우 찾기
def solution(x, y, field):
  global cnt

  # 가로부터 검사
  for i in range(n):
    

  pass



for i in range(n):
  for j in range(n):
    if field[i][j] == '1':
      solution(i, j, field[:])