import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for xi, yi in points:
            distance = (xi)**2 + (yi)**2

            if len(heap) < k: heapq.heappush(heap, (-distance, [xi,yi]))
            else: heapq.heappushpop(heap, (- distance,[xi,yi]))
            
        return [h[1] for h in heap]
