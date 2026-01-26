from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)

        max_heap = []
        for count in freq.values():
            heapq.heappush(max_heap, -count)

        cooldown_q = deque()
        time = 0

        while max_heap or cooldown_q:
            time += 1

            while cooldown_q and cooldown_q[0][0] <= time:
                available_time, cnt = cooldown_q.popleft()
                heapq.heappush(max_heap, cnt)

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  
                if count < 0:
                    cooldown_q.append((time + n + 1, count))

        return time
