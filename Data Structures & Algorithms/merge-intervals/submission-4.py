class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda t: t[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start > last_end:
                output.append([start, end])
            else:
                output[-1][1] = max(output[-1][1], end)

        return output