class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        i,j = 1,2
        min_sum = float('inf')
        while i < len(nums)-1:
            j = i+1
            r_sum = 0
            while j < len(nums):
                r_sum = nums[0]+ nums[i] + nums[j]
                if r_sum < min_sum:
                    min_sum = r_sum
                j +=1
            i+= 1
        return min_sum







        