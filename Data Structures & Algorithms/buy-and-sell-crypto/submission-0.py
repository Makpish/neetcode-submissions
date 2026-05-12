class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cmin = prices[0]
        m = 0
        for i in range(1,len(prices)):
            m = max(m, prices[i]-cmin)
            cmin = min(cmin, prices[i])
            # print(cmin,m)
        return m
        