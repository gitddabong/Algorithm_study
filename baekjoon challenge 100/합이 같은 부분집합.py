import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# n = int(input())
# nums = list(map(int, input().split()))
# sumAll = sum(nums)

# flag = False
# def dfs(limit, idx = 0, total = 0, depth = 0):
#   global flag
#   if depth == limit:
#     if total * 2 == sumAll:
#       print("YES")
#       exit()
#       # flag = True
#     return

#   for i in range(idx, n):
#     dfs(limit, i + 1, total + nums[i], depth + 1)

# for i in range(1, n // 2 +1):
#   dfs(i)
#   if flag == True:
#     break

# if flag:
#   print("YES")
# else:
#   print("NO")




def DFS(L, sum):
    if sum > total // 2:
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0) # 프로그램 종료시킴
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")