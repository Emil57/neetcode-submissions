from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1

        rows, cols = len(grid), len(grid[0])
        minutes, fresh = 0, 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: queue.append((r,c))
                if grid[r][c] == 1: fresh += 1
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr,nc = dr+r, dc+c
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))
            minutes += 1
        return minutes if fresh == 0 else -1


    



