from heapq import heappush, heappop
from collections import deque

def solution(jobs):
    answer = 0
    result = []
    
    jobs = deque(sorted(jobs, key=lambda x: x[0]))
    length = len(jobs)
    i = 0
    heap = []
    cur = 0
    while i < length:
        while jobs and jobs[0][0] <= cur:
            arrived, time = jobs.popleft()
            heappush(heap, (time, arrived))
        
        if heap:
            time, arrived = heappop(heap)
            cur += time
            result.append(cur - arrived)
            i += 1
        else:
            cur += 1
        
        # print(jobs)
        
        # print(cur)
        
    
    
    return sum(result) // length