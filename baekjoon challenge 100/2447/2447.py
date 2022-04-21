# import sys
# import math

# def printStar(depth, isCenter = False):
#   if depth == 0:
#     if isCenter:
#       print(' ', end="")
#       return
#     else:
#       print('*', end="")
#       return
  
#   printStar(depth - 1, False)
#   printStar(depth - 1, False)
#   printStar(depth - 1, False)

#   print()

#   printStar(depth - 1, False)
#   printStar(depth - 1, True)
#   printStar(depth - 1, False)

#   print()

#   printStar(depth - 1, False)
#   printStar(depth - 1, False)
#   printStar(depth - 1, False)


# if __name__ == "__main__":
#   input = sys.stdin.readline
#   n = int(input())
#   log_n = int(math.log(n, 3))

#   array = [[" "] * n for _ in range(n)]

#   printStar(n)



import sys
sys.setrecursionlimit(10**6)

def append_star(LEN):
  if LEN == 1:
    return ['*']

  Stars = append_star(LEN // 3)
  L = []

  for S in Stars:
    L.append(S*3)
  for S in Stars:
    L.append(S + ' ' * (LEN // 3) + S)
  for S in Stars:
    L.append(S*3)
  return L

if __name__ == "__main__":
  input = sys.stdin.readline
  n = int(input())
  print('\n'.join(append_star(n)))

# import sys

# input = sys.stdin.readline

# def append_star(length):
#   if length == 1:
#     return ['*']


  