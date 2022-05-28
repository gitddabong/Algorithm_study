# input
# P = "82195", S = "64723"
# output
# 13

if __name__ == "__main__":
  # P = "82195"
  # S = "64723"
  P = "00000000000000000000"
  S = "91919191919191919191"

  # 정, 역 방향 구하는 조건 - 생각해보니까 정방향 역방향은 구할 필요가 없구나
  # 1. 우선 두 수의 차를 구한다.
  # 2. 두 수의 차를 temp라고 하면, min(temp, 10-temp) 를 카운트에 추가

  result = 0
  for i in range(len(P)):
    temp = abs(int(P[i]) - int(S[i]))
    result += min(temp, 10 - temp)

  print(result)