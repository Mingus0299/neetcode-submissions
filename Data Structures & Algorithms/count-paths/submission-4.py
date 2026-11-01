class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * (n+1)
        row[n-1] = 1

        for r in range(m-1, -1, -1):

            for c in range(n-1, -1, -1):
                row[c] += row[c+1]

        return row[0]

