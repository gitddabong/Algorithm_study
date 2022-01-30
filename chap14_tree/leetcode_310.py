class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        # 리프 노드들을 하나씩 제거하면서 루트의 후보를 정함.
        
        
        # 예외 처리
        if n <= 1:
            return [0]
        
        # 인접 리스트에 추가
        graph = collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        # 리프 노드들 따로 저장. 길이가 1이라는 뜻은 연결된 노드가 1개밖에 없다 = 리프노드
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)
                
        while n > 2:    # 트리가 최소 높이가 되려면 가장 중심부에 있는 노드 1개나 2개만 후보가 됨.
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:     # 리프 노드 삭제
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:   # 새로 리프노드가 된 노드들을 new_leaves에 저장
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
            
        return leaves
        
        
        