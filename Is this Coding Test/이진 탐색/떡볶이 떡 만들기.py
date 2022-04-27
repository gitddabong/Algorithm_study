n, m = map(int, input().split())

nums = list(map(int, input().split()))

mid = sum(nums) // n
while True:
  total = 0
  for num in nums:
    if num > mid:
      total += num - mid
  
  if total > m:
    mid += 1
  elif total < m:
    mid -= 1
  else:
    break

print(mid)