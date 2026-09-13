class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range (len(nums)):
            x = target - nums[i]
            if x in hash_map:
                return [i, hash_map[x]]
            hash_map[nums[i]] = i

        return -1         