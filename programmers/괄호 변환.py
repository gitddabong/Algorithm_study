from collections import deque

p = "((()))"

def isCorrectString(inputStr):
    stack = deque()
    for char in inputStr:
        stack.append(char)
        
        if len(stack) >= 2 and stack[-2] == "(" and stack[-1] == ")":
            # if stack[-1] == "(" and char == ")":
            stack.pop()
            stack.pop()
    
    if stack:
        return False
    else:
        return True

def getBalancedString(inputStr):
    cnt1 = cnt2 = 0
    
    for char in inputStr:
        if char == "(":
            cnt1 += 1
        else:
            cnt2 += 1
        
        if cnt1 != 0 and cnt2 != 0 and cnt1 == cnt2:
            return inputStr[:cnt1+cnt2], inputStr[cnt1+cnt2:]
        
    return "", inputStr


def recursion(p):
    if not p:
        return p
    
    u, v = getBalancedString(p)
    
    if isCorrectString(u):
        return u + recursion(v)
    
    else:
        if len(u) >= 2:
            temp = list(u[1:-1])
            for i in range(len(temp)):
                if temp[i] == "(":
                    temp[i] = ")"
                else:
                    temp[i] = "("
            temp = "".join(temp)
            temp = "(" + temp + ")"
        return temp + recursion(v)
        
def solution(p):
    answer = recursion(p)
    
    return answer

print(solution(p))