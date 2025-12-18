from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        
        # Base profit calculation
        profit = sum(prices[i] * strategy[i] for i in range(n))
        
        if k == 0 or n < k:
            return profit
        
        half = k // 2
        
        # For each index i, precompute:
        # A[i] = -strategy[i] * prices[i] (used when in first half of window)
        # B[i] = prices[i] - strategy[i] * prices[i] (used when in second half)
        A = [-strategy[i] * prices[i] for i in range(n)]
        B = [prices[i] - strategy[i] * prices[i] for i in range(n)]
        
        # Build prefix sums for efficient range queries
        prefixA = [0] * (n + 1)
        prefixB = [0] * (n + 1)
        for i in range(n):
            prefixA[i + 1] = prefixA[i] + A[i]
            prefixB[i + 1] = prefixB[i] + B[i]
        
        max_gain = 0
        
        # For each window starting at j
        for j in range(n - k + 1):
            # First half: indices [j, j+half)
            # Second half: indices [j+half, j+k)
            gain = 0
            if half > 0:
                gain += prefixA[j + half] - prefixA[j]
            if k > half:
                gain += prefixB[j + k] - prefixB[j + half]
            
            max_gain = max(max_gain, gain)
        
        return profit + max_gain