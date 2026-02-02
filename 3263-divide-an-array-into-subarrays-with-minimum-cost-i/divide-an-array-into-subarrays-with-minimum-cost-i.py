class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 3:
            return sum(nums)
        
        prefix_min = nums[1]
        ans = float('inf')
        
        for j in range(2, n):
            ans = min(ans, nums[0] + prefix_min + nums[j])
            prefix_min = min(prefix_min, nums[j])
        
        return ans
