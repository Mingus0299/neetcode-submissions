class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        maxn = arr[-1]

        for i in range (len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = maxn
            maxn = max(maxn, temp)

        arr[-1] = -1

        return arr