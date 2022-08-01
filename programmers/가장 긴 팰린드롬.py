from collections import deque
from copy import deepcopy

def isPalindrome(_str):
    return True if _str == _str[::-1] else False

def solution(s):
    answer = 1

#     q = deque(list(s))

#     while len(q) >= 3:
#         tmp = deepcopy(q)
#         for i in range(len(q)-1, 1, -1):
#             if isPalindrome("".join(tmp)):
#                 answer = max(answer, len(tmp))
#                 break
#             else:
#                 tmp.pop()

#         q.popleft()

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            _str = s[i:j]
            if isPalindrome(_str):
                answer = max(answer, len(_str))

    return answer