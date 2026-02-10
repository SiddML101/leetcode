class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_count = 0
        for i in range (len(nums)):
            hash_odd = {}
            hash_even = {}
            count = 0
            for j in range (i,len(nums)):
                if nums[j] % 2 == 0:
                    if nums[j] in hash_even:
                        hash_even[nums[j]] += 1
                    else:
                        hash_even[nums[j]] = 1
                else:
                    if nums[j] in hash_odd:
                        hash_odd[nums[j]] += 1
                    else:
                        hash_odd[nums[j]] = 1
                if len(hash_even) == len(hash_odd):
                    count = j-i +1
                    if max_count < count:
                        max_count = count
            
        return max_count
        