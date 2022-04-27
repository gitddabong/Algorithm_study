import sys
input = sys.stdin.readline
num = input().rstrip()
# num = list(map(str, num))
stack = []

for x in num:
    if x.isdecimal():   # 숫자이면
        stack.append(int(x))
    else:
        if len(stack) >= 2:
            if x == '*':
                stack.append(stack.pop(-2)*stack.pop())
            elif x == '/':
                stack.append(stack.pop(-2)/stack.pop())
            elif x == '+':
                stack.append(stack.pop(-2)+stack.pop())  
            else:
                stack.append(stack.pop(-2)-stack.pop())
print(stack)