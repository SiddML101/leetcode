class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        a = 1
        b = 1
        for i in range (n):
            prefix[i] = a
            a = a * nums[i]

        for j in range (n-1,-1,-1):
            suffix[j] = b
            b = b * nums[j]

        output = []
        for k in range (n):
            c = prefix[k] * suffix[k]
            output.append(c)

        return output
            
        
        
            