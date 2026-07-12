#leetcode 2492-minimum score of a path between two cities
#difficulty:medium
#approach:BFS
#time complexity:O(V+E)
#space complexity:O(V+E)
class Solution(object):
    def minScore(self, n, roads):
        graph = {}
        for u, v, w in roads:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        queue = [1]
        visited = set([1])
        min_score = float('inf')
        head = 0
        
        while head < len(queue):
            node = queue[head]
            head += 1
            
            if node not in graph:
                continue
                
            for neighbor, weight in graph[node]:
                if weight < min_score:
                    min_score = weight
                    
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score