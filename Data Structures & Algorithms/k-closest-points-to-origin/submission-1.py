import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x,y in points:
            d = x**2 + y**2
            if len(max_heap) < k: 
                heapq.heappush(max_heap,(-d,x,y))
            else: heapq.heappushpop(max_heap,(-d,x,y))
        return [(x,y) for d,x,y in max_heap]
        # Time O(n log k)
        # Space O(k)