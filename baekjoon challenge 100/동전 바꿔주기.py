# 입력 예제
# 20
# 3
# 5 3
# 10 2
# 1 5

# 출력 : 첫 줄에 받은 목표치를 만드는 모든 경우의 수

# def dfs(idx = 0, total = 0, result = []):
#   if total == target:
#     if result not in answer:
#       answer.append(result[:])
#     return

#   elif total > target:
#     return

#   for i in range(idx, len(nums)):
#     if total + sum(nums[idx:]) < target:
#       continue

#     result.append(nums[i])
#     dfs(i+1, total + nums[i], result)
#     result.pop(-1)

# target = int(input())
# n = int(input())
# nums = []
# for _ in range(n):
#   num, m = map(int, input().split())
#   for _ in range(m):
#     nums.append(num)
# # nums = [5,5,5,10,10,1,1,1,1,1]
    
# answer = []
# dfs()
# print(len(answer))

# def DFS(L, sum):
#     global cnt
#     if sum>m:
#         return
#     if L==n:
#         if sum==m:
#             cnt+=1
#     else:
#         for i in range(cn[L]+1):
#             DFS(L+1, sum+(cv[L]*i))

# m=int(input())
# n=int(input())
# cv=list()
# cn=list()
# for i in range(n):
#     a, b=map(int, input().split())
#     cv.append(a)
#     cn.append(b)
# cnt=0
# DFS(0, 0)
# print(cnt)

from collections import defaultdict

def dfs(L = 0, total = 0, depth = 0):
  global cnt
  if depth == len(coins):
    if total == target:
      cnt += 1
    return

  elif total > target:
    return

  for i in range(counts[coins[L]]+1):
    dfs(L+1, total + coins[L]*i, depth + 1)

target = int(input())
n = int(input())
coins = []
counts = defaultdict(int)
for _ in range(n):
  coin, m = map(int, input().split())
  coins.append(coin)
  counts[coin] = m

cnt = 0
dfs()
print(cnt)
