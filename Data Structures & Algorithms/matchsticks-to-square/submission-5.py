class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        target = sum(matchsticks) // 4
        used = [False] * len(matchsticks)
        
        def backtrack(i, g, sumsubset):
            if g == 0:
                return True

            if sumsubset == target:
                return backtrack(0, g-1, 0)

            for j in range(i, len(matchsticks)):
                if not used[j] and sumsubset + matchsticks[j] <= target:
                    used[j] = True
                    if backtrack(j+1, g, sumsubset+matchsticks[j]):
                        return True
                    used[j] = False

            return False

        return backtrack(0, 4, 0)



            