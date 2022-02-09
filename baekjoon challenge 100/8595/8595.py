import sys
import re
from collections import deque
input = sys.stdin.readline

n = int(input())
_str = input().rstrip()
q = deque()
# p = re.compile('[0-9]')
p = ['1','2','3','4','5','6','7','8','9','0']

result = 0
for char in _str:
    # 숫자가 들어오면 큐에 삽입
    if char in p:
        q.append(char)
    
    # 문자열인 경우
    else:
        if q:
            temp = ''
            while q:
                temp += q.popleft()
            result += int(temp)
            
if q:
    temp = ''
    while q:
        temp += q.popleft()
    result += int(temp)

print(result)