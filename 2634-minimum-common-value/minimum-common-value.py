class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i,j = 0,0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] > nums2[j]:
                if j+1 < len(nums2):
                    j+=1
                else:
                    break
            if nums1[i] < nums2[j]:
                if i+1 < len(nums1):
                    i+=1
                else: 
                    break

        return -1
        