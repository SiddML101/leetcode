class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 3:
            return min(height) * 1
        i = 0
        j = len(height) - 1
        count = 0
        max_count = 0
        h = 0
        while i < j:
            h = min(height[i], height[j])
            count  = h * (j-i)
            if count > max_count:
                max_count = count
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_count

            

        