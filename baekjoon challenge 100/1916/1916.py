import sys
input = sys.stdin.readline

from heapq import heappush, heappop

n = int(input())
testcase = int(input())

graph = [[] for _ in range(n+1)]

for i in range(testcase):
  src, des, cost = map(int, input().split())
  graph[src].append([des, cost])
  
start, end = map(int, input().split())

dp = [float('inf')] * (n+1)

def dijkstra(start):
  dp[start] = 0
  heap = []
  heappush(heap, [0, start])  # 초기값
  while heap:
    w, n = heappop(heap)
    if dp[n]< w:
      continue
    
    for n_n, n_w in graph[n]:
      sum_w = w + n_w
      if dp[n_n] < sum_w:
        dp[n_n] = sum_w
        heappush(heap, [sum_w, n_n])

dijkstra(start)
print(dp[end])
    
# import sys
# from heapq import heappush, heappop

# n = int(input())
# m = int(input())
# inf = 100000000
# s = [[] for i in range(n + 1)]  # 인접 리스트
# dp = [inf for i in range(n + 1)]    # 시작점에서 각 노드별 최소 거리를 저장하는 리스트
# for i in range(m):
#   a, b, w = map(int, input().split())
#   s[a].append([b, w])
# start, end = map(int, input().split())

# def dijkstra(start):
#   dp[start] = 0
#   heap = []
#   heappush(heap, [0, start])  # 초기값
#   while heap: 
#     w, n = heappop(heap)
#     if dp[n] < w:   # 현재 노드의 저장된 최솟값과 리스트에서 받아온 거리값과 비교해서 받은 값이 작을 경우 리스트 업데이트
#       continue
#     for n_n, wei in s[n]:   # 인접한 노드 번호와 코스트 받아오기
#       n_w = w + wei   # 인접 노드를 합쳐서 만든 거리
#       if dp[n_n] > n_w:   # 합쳐서 만든 거리가 더 작으면 최솟값 갱신
#         dp[n_n] = n_w
#         heappush(heap, [n_w, n_n])  # 새로 만든 최솟값으로 새로 푸시

# dijkstra(start)
# print(dp[end])
