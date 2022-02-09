# 시간 초과

# import sys
# input = sys.stdin.readline

# _str = list(input().rstrip())
# n = int(input())
# cursor = len(_str)

# for _ in range(n):
#     cmd = list(input().split())
    
#     if cmd[0] == "L":
#         if cursor > 0:
#             cursor -= 1
#     elif cmd[0] == "D":
#         if cursor < len(_str):
#             cursor += 1
#     elif cmd[0] == "B":
#         if cursor > 0:
#             cursor -= 1
#             _str.pop(cursor)
#     elif cmd[0] == "P":
#         _str.insert(cursor, cmd[1])
#         cursor += 1

# print("".join(_str))

import sys
from collections import deque
input = sys.stdin.readline

stack1 = deque(list(input().rstrip()))
stack2 = deque()
n = int(input())

for _ in range(n):
    cmd = list(input().split())
    
    if cmd[0] == "L":
        if stack1:
            stack2.appendleft(stack1.pop())
    elif cmd[0] == "D":
        if stack2:
            stack1.append(stack2.popleft())
    elif cmd[0] == "B":
        if stack1:
            stack1.pop()
    elif cmd[0] == "P":
        stack1.append(cmd[1])

result = stack1 + stack2
print("".join(result))
