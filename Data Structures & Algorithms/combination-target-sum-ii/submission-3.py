class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtracking(i, cur, total):
            if total == target:
                ans.append(cur.copy())
                return

            if i == len(candidates) or total > target:
                return

            for j in range(i, len(candidates)):

                if (j>i and candidates[j] == candidates[j-1]):
                    continue

                cur.append(candidates[j])

                backtracking(j+1, cur, total+candidates[j])
                cur.pop()

        backtracking(0, [], 0)
        return ans



            