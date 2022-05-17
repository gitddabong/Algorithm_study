n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

checklist = [False] * (n+1)
def dfs(node):
  checklist[node] = True
  for next in graph[node]:
    if checklist[next] == False:
      dfs(next)

dfs(1)
checklist[1] = False
result = 0
for check in checklist:
  if check:
    result += 1
print(result)
