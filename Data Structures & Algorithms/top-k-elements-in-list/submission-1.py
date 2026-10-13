import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, v in counter.items():
            if len(heap) < k: heapq.heappush(heap,(v,key))
            else: heapq.heappushpop(heap, (v,key))

        elements = [h[1] for h in heap]
        return elements