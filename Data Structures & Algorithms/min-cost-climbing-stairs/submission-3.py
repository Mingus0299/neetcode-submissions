class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min (cost[0], cost[1])


# [10, 20, 5, 5, 20] 0 ]
# [0, 0, 0, 0]
# [0, 0, 10, 15, 15, 20]



# [10, 20, 10, 5, 20] 0 ]
# [10, 25, 10, 5 20] 0]
# [20, 25, 10, 5, 20] 0]

# 
