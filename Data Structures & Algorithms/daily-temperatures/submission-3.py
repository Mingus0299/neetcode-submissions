class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #index, temperatures
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                index, temp = stack.pop()
                res[index] = i - index
            stack.append([i, temperatures[i]])

        return res