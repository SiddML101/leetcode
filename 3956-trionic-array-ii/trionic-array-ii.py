class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**18

        up = [-INF] * n
        down = [-INF] * n
        up2 = [-INF] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(nums[i - 1] + nums[i], up[i - 1] + nums[i])

            if nums[i] < nums[i - 1]:
                if up[i - 1] != -INF:
                    down[i] = up[i - 1] + nums[i]
                if down[i - 1] != -INF:
                    down[i] = max(down[i], down[i - 1] + nums[i])

            if nums[i] > nums[i - 1]:
                if down[i - 1] != -INF:
                    up2[i] = down[i - 1] + nums[i]
                if up2[i - 1] != -INF:
                    up2[i] = max(up2[i], up2[i - 1] + nums[i])

        return max(up2)
