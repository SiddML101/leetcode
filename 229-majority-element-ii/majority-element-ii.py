class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums) // 3
        hash_map = {}
        arr = []

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        for key in hash_map:
            if hash_map[key] > n:
                arr.append(key)

        return arr