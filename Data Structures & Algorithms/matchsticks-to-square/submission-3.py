class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        target = sum(matchsticks) // 4
        groups = [0] * 4

        matchsticks.sort(reverse=True)

        def dfs(i, groups):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if groups[j] + matchsticks[i] <= target:
                    groups[j]+= matchsticks[i]
                    if dfs(i+1, groups):
                        return True
                    groups[j]-= matchsticks[i]
            return False

        return dfs(0, groups)
