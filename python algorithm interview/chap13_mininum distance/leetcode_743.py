class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # k에서 시그널을 보내 모든 노드가 시그널을 받는 시간을 출력하는 것이니
        # 모든 경로에서 걸리는 시간의 최댓값을 출력하면 되겠구나
        # 한 노드라도 경로가 끊겨 있어서 못 가는 상황이 발생하면 -1 출력하고 프로그램 종료
        
        def dijkstra(start):
            dp[0] = dp[start] = 0
            heap = []
            heapq.heappush(heap, (0, start))
            
            while heap:
                time, node = heapq.heappop(heap)
                if dp[node] < time:     # 현재 리스트에 들어 있는 최솟값이 더 작으면 이 경우는 알고리즘을 수행할 필요가 없음.
                    continue
                    
                for n_node, t in graph[node]:
                    n_time = time + t
                    if dp[n_node] > n_time:
                        dp[n_node] = n_time
                        heapq.heappush(heap, [n_time, n_node])
                    
        graph = collections.defaultdict(list)
        for src, des, dist in times:
            graph[src].append([des, dist])
            
        dp = [float('inf')] * (n + 1)   # 각 경로를 탐색할 때 걸리는 시간을 저장
        
        dijkstra(k)
        max_val = max(dp)
        return -1 if max_val == float('inf') else max_val