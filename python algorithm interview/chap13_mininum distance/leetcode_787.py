class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
        graph = collections.defaultdict(list)
        # 인접 리스트
        for u, v, w in flights:
            graph[u].append((v,w))
            
        
        # 큐 변수 [(가격, 정점, 남은 가능 경우지 수)]
        Q = [(0, src, K)]

        # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)   # 비용이 가장 낮은 노드를 pop하면서 방문. 
            if node == dst:     # 목적지를 만나면 비용 return. 여기서 바로 리턴 해줘도 되는 이유는 최소 힙에서 최솟값만 골라서 방문하고 있기 때문.
                return price
        
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k-1))    # 힙에 비용은 더하고, 카운트는 낮춰서 삽입
                    
        return -1
        
        
        
        
        
        
        
        
        
        
#         sys.setrecursionlimit(10**8)
        
#         # dfs 순회로 구현.
#         # k를 depth를 이용한 종료 조건으로 사용하고 추가적인 테이블 없이 최소 거리만 저장해도 될 것 같다
        
#         # 다른 자료구조 없이 이렇게 하면 시간 초과 뜬다
#         self.min_dist = float('inf')
        
#         def dfs(curr, total_dist = 0, depth = -1):
#             if depth <= k:
#                 if curr == dst:
#                     self.min_dist = min(self.min_dist, total_dist)
#                     # if min_dist >= total_dist:
#                     #     min_dist = total_dist
#                     return
            
#             for node, dist in graph[curr]:
#                 dfs(node, total_dist + dist, depth + 1)
            
#         graph = collections.defaultdict(list)
#         for a, b, dist in flights:
#             graph[a].append([b, dist])
                    
#         dfs(src)
#         return -1 if self.min_dist == float('inf') else self.min_dist
        