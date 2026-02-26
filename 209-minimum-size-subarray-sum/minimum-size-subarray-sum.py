from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        total = 0
        min_len = float('inf')
        
        for j in range(len(nums)):
            total += nums[j]
            
            while total >= target:
                min_len = min(min_len, j - i + 1)
                total -= nums[i]
                i += 1
        
        return 0 if min_len == float('inf') else min_len