class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        ans = 0

        while (sell < len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell

            ans = max(ans, prices[sell]-prices[buy])
            sell+=1

        return ans