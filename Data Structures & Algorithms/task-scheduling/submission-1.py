import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        
        max_heap = [-c for l, c in counter.items()]
        heapq.heapify(max_heap)
        queue = deque()
        time = 0
        while max_heap or queue:
            time+=1
            if max_heap:
                task = 1 + heapq.heappop(max_heap)
                if task:
                    queue.append((task, time+n))
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap,queue.popleft()[0])
        return time
        # Time O(log n)
        # Space O(n)