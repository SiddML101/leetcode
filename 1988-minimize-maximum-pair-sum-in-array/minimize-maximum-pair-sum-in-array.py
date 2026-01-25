class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        nums.sort()
        i ,j = 0, len(nums)-1
        pair_sum = 0
        max_pair_sum = 0
        while i < j:
            pair_sum = nums[i] + nums[j]
            if pair_sum > max_pair_sum:
                max_pair_sum = pair_sum
            i += 1
            j -= 1

        return max_pair_sum
            

        