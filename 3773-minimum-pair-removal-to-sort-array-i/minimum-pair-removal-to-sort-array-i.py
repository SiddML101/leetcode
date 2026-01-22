class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        while True:
            sorted_nums = True
            for i in range (len(nums)-1):
                if nums[i] > nums[i+1]:
                    sorted_nums = False
                    break
            if sorted_nums:
                return ops
            
            min_sum = nums[0] + nums[1]
            min_idx = 0
            for i in range (len(nums)-1):
                if nums[i] + nums[i+1] < min_sum:
                    min_sum = nums[i] + nums[i+1]
                    min_idx = i
            nums[min_idx] = min_sum
            nums.pop(min_idx+1)

            ops += 1