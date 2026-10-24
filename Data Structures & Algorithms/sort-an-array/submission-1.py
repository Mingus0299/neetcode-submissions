class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, L, R, M):
            left_arr, right_arr = arr[L:M+1], arr[M+1:R+1]
            left, right, curr = 0 , 0, L


            while left < len(left_arr) and right < len(right_arr):
                if left_arr[left] < right_arr[right]:
                    arr[curr] = left_arr[left]
                    left+=1

                else:
                    arr[curr] = right_arr[right]
                    right+=1

                curr+=1

            while left < len(left_arr):
                arr[curr] = left_arr[left]
                curr+=1
                left+=1

            while right < len(right_arr):
                arr[curr] = right_arr[right]
                curr+=1
                right+=1


        def mergeSort(arr, l, r):
            if l == r:
                return arr

            m = (l+r) // 2

            mergeSort(arr, l , m)
            mergeSort(arr, m+1 , r)

            merge(arr, l, r, m)
            return arr

        return mergeSort(nums, 0, len(nums)-1)
