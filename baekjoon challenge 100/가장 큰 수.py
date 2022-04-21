from collections import deque

inp1, inp2 = input().split()

nums = deque(list(map(int, inp1)))
nums_len = len(nums)
n = int(inp2)
stack = deque()

cnt = 0
while len(stack) < nums_len - n:
  temp = nums.popleft()
  while stack and stack[-1] < temp and cnt < n:
    stack.pop()
    cnt += 1
  
  stack.append(temp)

if nums:
  for num in nums:
    if stack[-1] < num:
      stack.pop()
      stack.append(num)

print(stack)  