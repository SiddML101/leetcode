class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        i,j = 1,2
        a = nums[i]
        min_sum = float('inf')
        while j < len(nums):
            r_sum = nums[0] + a + nums[j]
            if r_sum < min_sum:
                min_sum = r_sum
            j += 1
            i += 1
            if nums[i] < a:
                a = nums[i]

        return min_sum







        