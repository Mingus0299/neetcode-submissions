class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n != 0 else 0
        lst = [0] * (n+1)
        
        lst[1] = 1
        lst[2] = 1

        for i in range(3, n+1):
            lst[i] = lst[i-3] + lst[i-2] + lst[i-1]

        return lst[n]