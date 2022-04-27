import sys

if __name__ == "__main__":
  input = sys.stdin.readline

  n = int(input())
  k = int(input())

  left = 1
  right = n**2
  result = 0

  while left < right:
    mid = (left + right) // 2
    
    cnt = 0
    for i in range(1, n+1):
      if mid > n * i:   # mid가 그 현재 행의 최댓값보다 큰 경우 행 길이만큼만 카운트 더하기
        cnt += n
      else:
        cnt += mid // i   # mid // i 는 현재 행에서 mid보다 작은 수의 개수
    
    # result = mid

    if cnt >= k:
      right = mid
    else:
      left = mid + 1

  print(left)
  