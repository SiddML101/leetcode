class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        hash_map = {}
        for i in range (len(nums1)):
            if nums1[i] not in hash_map:
                hash_map[nums1[i]] = 1

            else:
                hash_map[nums1[i]] += 1
        
        nums3 = []

        for i in range (len(nums2)):
            if nums2[i] in hash_map:
                nums3.append(nums2[i])

        if len(nums3) == 0:
            return -1

        return nums3[0]
        