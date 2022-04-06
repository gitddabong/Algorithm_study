cnt = 0
def dfs(numbers, target, depth, result):
  global cnt
  if depth == len(numbers):
    if result == target:
      cnt += 1
    
    return

  dfs(numbers, target, depth + 1, result + numbers[depth])
  dfs(numbers, target, depth + 1, result + numbers[depth]*(-1))

numbers = [4,1,2,1]
target = 4

dfs(numbers, target, 0, 0)

print(cnt)