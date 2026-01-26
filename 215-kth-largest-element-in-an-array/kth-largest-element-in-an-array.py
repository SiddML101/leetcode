class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort(reverse = True)
        for i in range (len(nums)):
            k -= 1
            if k == 0:
                return nums[i]

        return False