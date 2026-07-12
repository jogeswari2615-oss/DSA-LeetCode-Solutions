#leetcode 2685-count the number of complete components 
#difficulty:medium
#approach:BFS
#timecomplexity:O(n+m)
#space complexity:O(n+m)
class Solution(object):
    def countCompleteComponents(self, n, edges):
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components = 0
        
        for i in xrange(n):
            if not visited[i]:
                queue = [i]
                visited[i] = True
                
                component_vertices = 0
                component_edges = 0
                
                head = 0
                while head < len(queue):
                    curr = queue[head]
                    head += 1
                    
                    component_vertices += 1
                    component_edges += len(adj[curr])
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                if component_edges == component_vertices * (component_vertices - 1):
                    complete_components += 1
                    
        return complete_components