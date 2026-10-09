class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * (len(temperatures))
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                st_index, st_temp = stack.pop()
                res[st_index] = i - st_index

            stack.append([i, temp])

        return res