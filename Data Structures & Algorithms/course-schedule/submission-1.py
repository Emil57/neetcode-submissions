class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a,b in prerequisites: 
            g[a].append(b)
        
        VISITED = 2
        VISITING = 1
        UNVISITED = 0
        states = [UNVISITED] * numCourses

        def dfs(node):
            if states[node] == VISITED: return True
            elif states[node] == VISITING: return False

            states[node] = VISITING

            for n in g[node]:
                if not dfs(n): return False
            states[node] = VISITED
            return True
        for n in range(numCourses):
            if not dfs(n): return False
        
        return True

        # Time O(n)
        # Space O(n)