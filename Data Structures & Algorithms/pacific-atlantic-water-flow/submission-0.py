from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue, p_seen = deque(), set()
        a_queue, a_seen = deque(), set()

        rows, cols = len(heights), len(heights[0])

        for i in range(cols):
            p_queue.append((0,i))
            p_seen.add((0,i))

        for i in range(1,rows):
            p_queue.append((i,0))
            p_seen.add((i,0))
        
        for i in range(cols):
            a_queue.append((rows-1, i))
            a_seen.add((rows-1,i))

        for i in range(rows-1):
            a_queue.append((i,cols-1))
            a_seen.add((i,cols-1))

        def get_coords(queue, seen):
            coords = set()
            while queue:
                i, j = queue.popleft()
                coords.add((i,j))
                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    r, c = i+dr, j+dc
                    
                    if r in range(rows) and c in range(cols) and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        queue.append((r,c))
                        seen.add((r,c))
            return coords
        
        p_coords = get_coords(p_queue, p_seen)
        a_coords = get_coords(a_queue, a_seen)

        return list(p_coords.intersection(a_coords))