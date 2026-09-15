class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        if len(nums) < 2:
            return 1
        nums = list(set(nums))
        nums.sort()

        i,j = 0,1
        count = 0
        max_count = 0
        while j < len(nums):
            if nums[j] - nums[i] == 1:
                count += 1
                i += 1
                j += 1
            elif nums[j] - nums[i] != 1:
                count = 0
                i += 1
                j += 1

            if count > max_count:
                max_count = count


        return max_count + 1





        
        