n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n

dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
for i in range(2, n):
  dp[i] = max(nums[i] + nums[i-2], nums[i-1])

print(dp[n-1])