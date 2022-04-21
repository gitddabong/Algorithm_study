import sys

if __name__ == "__main__":
  input = sys.stdin.readline
  n, m = map(int, input().split())
  brs = list(map(int, input().split()))
  
  left = max(brs)
  right = sum(brs)
  result = float('inf')

  while left <= right:
    mid = (left + right) // 2
    cnt = 0
    total = 0
    for num in brs:
      total += num
      if total > mid:
        cnt += 1
        total = num
    
    if total:
      cnt += 1

    if cnt > m:
      left = mid + 1
    else:
      result = min(result, mid)
      right = mid - 1

  print(result)