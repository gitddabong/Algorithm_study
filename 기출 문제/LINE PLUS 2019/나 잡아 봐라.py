# # https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/
# from collections import deque

# def solution(C, B):
#   visited = [False] * 200001
#   q = deque()
#   q.append((B, 0))
  
#   result = 0
#   while q:
#     b_posi, cnt = q.popleft()
#     visited[b_posi] = True

#     c_posi = C + (cnt * (cnt + 1)) // 2
#     if c_posi > 200000:
#       return -1

#     if c_posi == b_posi:
#       result = cnt
#       break
#     else:
#       if 0 <= b_posi - 1 and not visited[b_posi - 1]:
#         q.append((b_posi - 1, cnt + 1))
#       if b_posi + 1 < 200000 and not visited[b_posi + 1]:
#         q.append((b_posi + 1, cnt + 1))
#       if b_posi * 2 < 200000 and not visited[b_posi * 2]:
#         q.append((b_posi * 2, cnt + 1))

#   return result

# print(solution(11, 2))


# https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/
import sys
from collections import deque
# input = sys.stdin.readline
# c, b = map(int, input().split())
c, b = 11, 2 # 3
# 반례1) c, b = 11, 1 # 6
# 반례2) c, b = 6, 3  # 4
Brown = []
ch = [0]*200001
visited = [False] * 200001
Brown = deque(Brown)
n = 0
# ch[b] = 0
Brown.append(b)

while Brown:
    now = Brown.popleft()
    visited[now] = True

    # cnt = ch[now]
    # c_cur = c + cnt * (cnt + 1) // 2

    if now == c:
        break

    for next in (now-1, now+1, now*2):
        if 0 <= next <= 200000:
            if not visited[next]:
                Brown.append(next)
                ch[next] = ch[now]+1
    if ch[next] > n+1:
        n += 1
        c = c+n
        
print(ch[now])