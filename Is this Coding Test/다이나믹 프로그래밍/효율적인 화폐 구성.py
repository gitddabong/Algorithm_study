n, m = map(int, input().split())
dp = [10001] * (m+1)
nums = []
for _ in range(n):
  num = int(input())
  nums.append(num)
  if num <=  m:
    dp[num] = 1

dp[0] = 0

for num in nums:
  for i in range(num, m + 1):
    dp[i] = min(dp[i], dp[i-num] + 1)
      
result = dp[m]
if result != 10001:
  print(result)
else:
  print(-1)
