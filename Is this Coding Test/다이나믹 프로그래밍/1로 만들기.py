n = int(input())
dp = [0] * (n+1)

for target in range(2, n + 1):
  temp = float('inf')
  if target % 5 == 0:
    temp = min(temp, dp[target // 5])
  if target % 3 == 0:
    temp = min(temp, dp[target // 3])
  if target % 2 == 0:
    temp = min(temp, dp[target // 2])
  temp = min(temp, dp[target - 1])
  dp[target] = temp + 1

print(dp[n])