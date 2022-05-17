n, m = map(int, input().split())
balls = list(map(int, input().split()))

# cnt = 0
# for i in range(n-1):
#   for j in range(i+1, n):
#     if balls[i] == balls[j]:
#       continue
#     cnt += 1
# print(cnt)

array = [0] * 11
for ball in balls:
  array[ball] += 1

result = 0
for i in range(1, m + 1):
  n -= array[i]
  result += array[i] * n

print(result)