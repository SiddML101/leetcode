class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}

        for j in range(min(k + 1, len(nums))):
            if nums[j] in hash_map:
                return True
            hash_map[nums[j]] = 1

        i = 0

        for j in range(k + 1, len(nums)):
            if hash_map[nums[i]] == 1:
                del hash_map[nums[i]]
            else:
                hash_map[nums[i]] -= 1

            i += 1

            if nums[j] in hash_map:
                return True

            hash_map[nums[j]] = 1

        return False