class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, r, mid):
            left_arr = arr[l:mid+1]
            right_arr = arr[mid+1:r+1]

            left, right, cur = 0, 0, l

            while left < len(left_arr) and right < len(right_arr):
                if left_arr[left] < right_arr[right]:
                    arr[cur] = left_arr[left]
                    left+=1

                else:
                    arr[cur] = right_arr[right]
                    right+=1

                cur+=1

            
            while left < len(left_arr):
                arr[cur] = left_arr[left]
                left+=1
                cur+=1

            while right < len(right_arr):
                arr[cur] = right_arr[right]
                right+=1
                cur+=1

            
        def mergeSort(arr, l, r):
            if l == r:
                return arr

            mid = (l+r)//2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid+1, r)

            merge(arr, l, r, mid)
            return arr

        return mergeSort(nums, 0, len(nums)-1)
