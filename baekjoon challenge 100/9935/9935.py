import sys
from collections import deque
input = sys.stdin.readline

_str = input().rstrip()
bomb = list(input().rstrip())

stack = deque()
for char in _str:
    stack.append(char)
        
    if char == bomb[-1] and len(stack) >= len(bomb):
        cnt = 0
        for i in range(1, len(bomb) + 1):
            if stack[-i] == bomb[-i]:
                cnt += 1
        
        if cnt == len(bomb):
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")


# 슬라이싱을 이용한 연산. 시간 초과뜸

# import sys
# from collections import deque
# input = sys.stdin.readline

# _str = input().rstrip()
# bomb = list(input().rstrip())

# stack = []
# for char in _str:
#     stack.append(char)
        
#     if char == bomb[-1]:
#         if stack[len(stack)-len(bomb):] == bomb:
#             stack = stack[:len(stack)-len(bomb)]

# if stack:
#     print("".join(stack))
# else:
#     print("FRULA")