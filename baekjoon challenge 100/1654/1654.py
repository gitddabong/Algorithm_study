import sys

if __name__ == "__main__":
  input = sys.stdin.readline

  n, k = map(int, input().split())

  cables = []
  for _ in range(n):
    cables.append(int(input()))

  right = sum(cables)
  left = 1
  result = 0

  while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for cable in cables:
      cnt += cable // mid

    if cnt >= k:
      left = mid + 1
      result = max(result, mid)
    else:
      right = mid - 1

  print(result)