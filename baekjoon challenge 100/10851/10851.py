import sys

if __name__ == "__main__":
  input = sys.stdin.readline
  n = int(input())
  data = list(map(int, input().split()))
  nums = sorted(data)

  m = int(input())
  targets = list(map(int, input().split()))

  # for target in targets:
  #   arr = nums[:]
  #   while arr:
  #     mid = len(arr) // 2
  #     if arr[mid] == target:
  #       print(1, end=" ")
  #       break
  #     elif arr[mid] < target:
  #       arr = arr[mid+1:]
  #     else:
  #       arr = arr[:mid]

  #   if arr:
  #     continue
  #   else:
  #     print(0, end=" ")

  for target in targets:
    left_i = 0
    right_i = n - 1
    flag = False
    while left_i <= right_i:
      mid = (left_i + right_i) // 2
      
      if nums[mid] == target:
        print(1, end=" ")
        flag = True
        break
      elif nums[mid] < target:
        left_i = mid + 1
      else:
        right_i = mid - 1
    if flag:
      continue
    else:
      print(0, end=" ")

# 왜 슬라이싱으로는 안되고 인덱스로는 되는가?
# 왜냐면 슬라이싱 시간복잡도는 O(n)이고 인덱스 바꾸는건 O(1)이니까
