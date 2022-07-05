from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    
    heap = []
    for num in scoville:
        heappush(heap, num)
    
    while heap[0] < K and len(heap) >= 2:
        tmp = heappop(heap) + heappop(heap) * 2
        heappush(heap, tmp)
        answer += 1
    
    if len(heap) < 2 and heap[0] < K:
        return -1
    
    return answer