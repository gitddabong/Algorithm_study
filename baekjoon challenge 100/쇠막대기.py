# testcase : ()(((()())(())()))(())

from collections import deque

_str = input()

stack = deque()

result = 0
last_char = ''
for char in _str:
  if char == '(':
    stack.append(char)
  else:
    stack.pop()
    if char == ')' and last_char == '(':
      result += len(stack)
    elif char == ')' and last_char == ')':
      result += 1
  
  last_char = char

print(result)
