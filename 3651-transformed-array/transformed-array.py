class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range (n):
            if nums[i] > 0:
                j = (i + nums[i])%n
                result.append(nums[j])
            if nums[i] < 0:
                j = (i - abs(nums[i]))%n
                result.append(nums[j])
            if nums[i] == 0:
                result.append(nums[i])

        return result

        