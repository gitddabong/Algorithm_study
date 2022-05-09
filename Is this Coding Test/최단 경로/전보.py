from heapq import heappush, heappop

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append([y, z])
INF = int(1e9)
d = [INF] * (n+1)

def dijkstra(start):
  heap = []
  d[start] = d[0] = 0
  heappush(heap, [0, start])
  
  while heap:
    c_cost, c_vtx = heappop(heap)
    if d[c_vtx] < c_cost:
      continue

    for n_vtx, n_cost in graph[c_vtx]:
      # start -> n_vtx 까지의 거리와
      # start -> c_vtx -> n_vtx 거리 중 최솟값 취하기
      dist1 = d[n_vtx]
      dist2 = d[c_vtx] + n_cost
      d[n_vtx] = min(dist1, dist2)
      heappush(heap, [d[n_vtx], n_vtx])

dijkstra(c)
cnt = 0
max_dist = 0
for dist in d:
  if dist == 0 or dist == INF:
    continue
  else:
    cnt += 1
    if max_dist < dist:
      max_dist = dist
print(cnt, max_dist)