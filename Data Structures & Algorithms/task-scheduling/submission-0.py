from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-c for c in counter.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0

        while maxHeap or queue:
            time+=1

            if maxHeap: 
                c = 1 + heapq.heappop(maxHeap)
                if c: 
                    queue.append([c,time+n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time