class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        i, j = 0, 0
        s1 = 0
        s2 = nums[0]

        while j < len(nums):
            s1 += nums[j]

            s2 = max(s2, s1)

            if s1 < 0:
                i = j + 1
                j = i
                s1 = 0
            else:
                j += 1

        return s2