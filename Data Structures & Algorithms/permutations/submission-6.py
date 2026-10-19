class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res = []

        def dfs(cur, lst_pick):
            
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(nums)):
                if not lst_pick[i]:
                    cur.append(nums[i])
                    lst_pick[i] = True
                    dfs(cur,lst_pick)
                    cur.pop()
                    lst_pick[i] = False

        dfs([], [False] * len(nums))
        return res