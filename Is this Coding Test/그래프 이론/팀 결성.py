n, m = map(int, input().split())

parent = [x for x in range(0, n+1)]

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

for _ in range(m):
  key, a, b = map(int, input().split())
  if key == 0:
    union_parent(parent, a, b)

  else:
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a == b:
      print("YES")
    else:
      print("NO")


# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1