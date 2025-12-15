class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        a = len(prices)
        if a == 1:
            return a

        streak = 1
        total = 1
        i = 1

        while i < len(prices):
            if prices[i-1] - prices[i] == 1:
                streak += 1
            else:
                streak = 1
            total += streak
            i += 1

        return total
