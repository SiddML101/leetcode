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
        j = k-1
        i = 0
        while j < len(nums):
            max_n = nums[j]
            min_n = nums[i]
            diff = max_n - min_n
            if diff < min_diff:
                min_diff = diff
            i += 1
            j += 1
            
        return min_diff
                
            




        