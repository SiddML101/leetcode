class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums[0]
        nums.sort()
        n = len(nums)
        min_n = nums[0]
        max_n = nums[n-1]
        i,j = 0,1
        arr =[]
        while j < n:
            if nums[j] - nums[i] == 1:
                j+=1
                i+=1
            else:
                for k in range (nums[i]+1,nums[j]):
                    arr.append(k)
                i += 1
                j += 1

        return arr




        


        
        