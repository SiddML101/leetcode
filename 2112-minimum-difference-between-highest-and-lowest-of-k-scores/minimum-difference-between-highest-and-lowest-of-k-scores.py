class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        if k == len(nums):
            return max(nums) - min(nums)
        diff = 0
        min_diff = float('inf')
        arr = []
        nums.sort()
        min_n = 0
        max_n = 0
        for i in range (len(nums)-k+1):
            for j in range (i, k+i):
                max_n = nums[j]
            min_n = nums[i]
            diff = max_n - min_n
            if diff < min_diff:
                min_diff = diff
            
        return min_diff
                
            




        