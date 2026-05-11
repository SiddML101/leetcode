class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range (len(nums)):
            a = str(nums[i])
            for digit in a:
                arr.append(int(digit))

        return arr
            


        