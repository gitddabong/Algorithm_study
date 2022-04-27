n, k = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort(reverse=True)

i = 0
while arr1[i] < arr2[i] and i < k:
  temp = arr1[i]
  arr1[i] = arr2[i]
  arr2[i] = temp
  i += 1

print(sum(arr1))