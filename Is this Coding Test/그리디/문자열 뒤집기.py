nums = input()

target = nums[0]
cnt = 0
temp = ""
for num in nums:
  if num == target:
    if temp:
      cnt += 1
      temp = ""
  else:
    temp = num

if temp:
  cnt += 1

print(cnt)