class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicate for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicate for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                k, l = j + 1, n - 1
                while k < l:
                    curr_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if curr_sum == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        # Move pointers and skip duplicates
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif curr_sum < target:
                        k += 1
                    else:
                        l -= 1
                        
        return result