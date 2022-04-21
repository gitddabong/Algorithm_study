# import sys
# sys.setrecursionlimit(10**9)

# def S(k, n):
#   if k == 1:
#     return n*(n+1) // 2
  
#   total = 0
#   for i in range(1, n+1):
#     total += S(k-1, i) % 1000000007

#   return total % 1000000007

# if __name__ == "__main__":
#   input = sys.stdin.readline

#   k, n = map(int, input().split())

#   print(S(k, n))


import sys

if __name__ == "__main__":
  input = sys.stdin.readline
  k, n = map(int, input().split())

  dp = [[0] * (n+1) for _ in range(k+1)]
  temp = int(1e9 + 7)

  for i in range(1, n+1):
    dp[0][i] = i

  for i in range(1, k+1):
    for j in range(1, n+1):
      dp[i][j] = (dp[i][j-1] % temp + dp[i-1][j] % temp) % temp

  print(dp[k][n])