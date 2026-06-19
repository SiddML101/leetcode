class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        count = 0
        max_count = 0
        for i in range (len(gain)):
            count += gain[i]
            if max_count < count :
                max_count = count

        return max_count
        