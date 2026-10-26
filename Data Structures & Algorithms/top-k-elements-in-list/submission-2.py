import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        min_heap = []
        counter = {}

        for n in nums:
            counter[n] = counter.get(n,0)+1
        
        for n, c in counter.items():
            if len(min_heap) < k: heapq.heappush(min_heap, (c,n))
            else: heapq.heappushpop(min_heap,(c,n))
        
        return [n for c,n in min_heap]
        # Time O(n log k )
        # Space O(k)