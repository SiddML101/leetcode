class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dist = 0
        max_dist = 0
        for i in range (len(colors)):
            for j in range (i,len(colors)):
                if colors[i] != colors[j]:
                    dist = j-i

                    if dist > max_dist:
                        max_dist = dist

        return max_dist

            


        