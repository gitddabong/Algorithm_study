n, m = map(int, input().split())

def find_parent(parent, e):
  if parent[e] != e:
    parent[e] = find_parent(parent, parent[e])
  return parent[e]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

parent = [x for x in range(n+1)]

edges = []
for _ in range(m):
  a, b, edge = map(int, input().split())
  edges.append((a, b, edge))
edges.sort(key = lambda x : x[2])

# 길이 짧은것부터 선택해서 parent 업데이트
# 두 정점이 같은 그룹일 경우 넘어가기
result = 0
result_edges = []
for a, b, edge in edges:
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  
  if a != b:
    result += edge
    result_edges.append(edge)
    union_parent(parent, a, b)
  else:
    continue

print(result - result_edges[-1])


    
  