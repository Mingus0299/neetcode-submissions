class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort(key = lambda t: t[0])
        for i in range(len(intervals)):
            if res and res[-1][1] >= intervals[i][0]:
                start, end = res.pop()
                new = [min(start, intervals[i][0]), max(end, intervals[i][1])]
                res.append(new)

            else:
                res.append(intervals[i])

        return res