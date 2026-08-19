class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        hash_map = {}

        for i in range(len(nums) - k + 1):
            window = set()

            for j in range(i, i + k):
                window.add(nums[j])

            for num in window:
                hash_map[num] = hash_map.get(num, 0) + 1

        ans = -1

        for key, value in hash_map.items():
            if value == 1:
                ans = max(ans, key)

        return ans