class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temperature, index
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while i > 0 and stack and temp > stack[-1][0]:
                tempe, index = stack.pop()
                output[index] = i-index
            stack.append([temp,i])

        return output

        