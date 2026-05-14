class Solution:
    def isGood(self, nums: List[int]) -> bool:
        hash_map = {}
        for i in range (len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] += 1
        
        n = len(nums)-1

        for i in range(1, n):
            if hash_map.get(i) != 1:
                return False

        if hash_map.get(n) != 2:
            return False

        return True

        