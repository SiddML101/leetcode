class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        if len(stones) <= 1:
            return stones[0]
        for i in range (len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
       
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x != y:
                diff = x - y
                stones.append(-diff)
                heapq.heapify(stones)
            
        if len(stones) == 0:
            return 0
        return -stones[0]
    



            
            