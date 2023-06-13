class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        x  = 0 
        max = 0
        for t in range(len(prices)):
            if prices[x] > prices[t]:
                x = t
            else:
                if prices[t] - prices[x] > max:
                    max = prices[t] - prices[x]
        return max
    
print(Solution().maxProfit([7,6,4,3,1]))