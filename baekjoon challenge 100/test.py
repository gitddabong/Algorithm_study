n = 5

arr = [[0] * 5 for _ in range(5)] 

num = 1
for i in range(5):
  for j in range(5):
    arr[i][j] = num
    print(num, end=" ")
    num += 1
  print()