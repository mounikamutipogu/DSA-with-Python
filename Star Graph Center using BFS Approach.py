class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        from collections import deque,defaultdict
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        start=-1
        mx=0
        for node in graph:
            if len(graph[node])>mx:
                mx=len(graph[node])
                start=node
        q=deque([start])
        visited={start}
        while q:
            node=q.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return start
        
