# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

v, e = map(int, input().split())
# graph = [[] for _ in range(v+1)]
edges = []
for _ in range(e):
  src, des, cost = map(int, input().split())
  edges.append((src, des, cost))
edges.sort(key = lambda x:x[2])
parents = [0] * (v+1)

def find_parent(parents, edge):
  if parents[edge] != edge:
    parents[edge] = find_parent(parents, parents[edge])
  return parents[edge]

def union_parent(parents, a, b):
  a = find_parent(parents, a)
  b = find_parent(parents, b)

  if a < b:
    parents[b] = a
  else:
    parents[a] = b

