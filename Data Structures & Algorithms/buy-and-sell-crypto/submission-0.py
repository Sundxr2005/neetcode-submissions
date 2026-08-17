class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        maxx = 0
        while len(prices) > r:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxx = max(profit, maxx)
            else:
                l = r
            r += 1
        return maxx



        