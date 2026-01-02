class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        d = {}
        for i in range (len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        
        a = max(d.values())
        for key,value in d.items():
            if a == value:
                return key
            
        