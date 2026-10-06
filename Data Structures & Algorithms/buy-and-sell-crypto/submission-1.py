class Solution:
    def maxProfit(self, prices: List[int]) -> int:

# sliding  buy, sell
# 

        buy = 0
        sell = 0
        answer = 0
        while(sell < len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell

            answer = max (answer, prices[sell] - prices[buy])

            sell+=1

        return answer