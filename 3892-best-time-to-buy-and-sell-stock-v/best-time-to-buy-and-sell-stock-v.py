class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        INF = float('-inf')
        free = [0] + [INF] * k
        lang = [INF] * (k+1)
        short = [INF] * (k+1)

        for price in prices:
            for t in range (k, -1, -1):
                lang[t] = max(lang[t], free[t] - price)
                short[t] = max(short[t], free[t] + price)

                if t+1 <= k:
                    free[t+1] = max(
                        free[t+1],
                        lang[t] + price,
                        short[t] - price 
                    )
        return max(free)
        