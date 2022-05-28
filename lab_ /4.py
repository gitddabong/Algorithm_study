def ant(text):
  result = ""
  temp = ""
  cnt = 0
  for char in text:
    if temp == char:
      cnt += 1
    else:
      # 다른 경우
      # 이전 cnt만큼 result에 추가
      if cnt != 0:
        result += temp + str(cnt)

      # 그리고 temp를 교체하고 cnt를 초기화
      temp = char
      cnt = 1

  if cnt != 0:
    result += temp + str(cnt)

  return result

def solution(n):
  d = ["1"] * 42
  d[2] = "11"
  for i in range(2, n+1):
    d[i+1] = ant(d[i])

  return d[n]

print(solution(5))