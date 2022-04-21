n = int(input())
r_nums = list(map(int,input().split()))
r_nums.insert(0, 0)

result = [0] * n

for i in range(1, n+1):
  target = r_nums[i]
  if result[0] == 0 and target == 0:
    result[0] = i
    continue

  cnt = 0
  idx = 0
  while True:
    if result[idx] == 0:
      cnt += 1
    idx += 1
    if result[idx] == 0 and cnt == target:
      break
  result[idx] = i

print(result)