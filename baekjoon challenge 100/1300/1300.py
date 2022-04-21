import sys

if __name__ == "__main__":
  input = sys.stdin.readline

  n = int(input())
  k = int(input())

  left = 1
  right = k
  result = 0

  while left < right:
    mid = (left + right) // 2
    
    cnt = 0
    for i in range(1, n+1):
      if mid > n * i:
        cnt += n
      else:
        cnt += mid // i
    
    # result = mid

    if cnt >= k:
      right = mid
    else:
      left = mid + 1

  print(left)
  