class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        state = 0
        if nums[1] < nums[0]:
            return False
        for i in range (len(nums)-1):
            if nums[i+1] == nums:
                return False

            if nums[i+1] == nums[i]:
                return False

            if state == 0 :
                if nums[i+1] > nums[i]:
                    continue
                else:
                    state += 1
            elif state == 1:
                if nums[i+1] < nums[i]:
                    continue
                else:
                    state += 1
            
            elif state == 2:
                if nums[i+1] > nums[i]:
                    continue
                else:
                    return False

        return state == 2