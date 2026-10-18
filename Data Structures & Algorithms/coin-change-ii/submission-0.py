class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

#                 amount
#            0, 1, 2, 3, 4, 5
#          1 1
# coins    2 1
#          5 1  
#          ? 1  0  0  0  0  0 

        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a]
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][amount]