from heapq import heappush, heappop, heapify

def solution(operations):    
    heap = []
    for operation in operations:
        order, num = operation.split()
        num = int(num)
        
        if order == 'I':
            heappush(heap, num)
        
        else:
            if heap:
                if num == 1:
                    heap.sort()
                    heap.pop(-1)
                    heapify(heap)
                else:
                    heappop(heap)
        print(heap)
                    
    # print(heap)
    min_val = max_val = 0
    if len(heap) >= 2:
        min_val = heappop(heap)
        heap.sort()
        max_val = heap.pop(-1)
    elif len(heap) == 1:
        min_val = max_val = heappop(heap)
                
    return [max_val, min_val]