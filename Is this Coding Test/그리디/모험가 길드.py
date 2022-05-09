from collections import deque
n = int(input())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
result = 0

q = deque(nums)
while q:
  temp = q.popleft()
  for _ in range(temp-1):
    if temp >= q[-1]:
      q.pop()
  result += 1

print(result)