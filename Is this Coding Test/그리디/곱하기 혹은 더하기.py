nums = list(input())

result = int(nums[0])
for i in range(1, len(nums)):
  if result == 0:
    result += int(nums[i])
  else:
    result *= int(nums[i])

print(result)