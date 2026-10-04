class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m, n, cur
        n-=1
        m-=1

        cur = len(nums1)-1
        while (m > -1 and n > -1):
            if (nums1[m] > nums2[n]):
                nums1[cur] = nums1[m]
                m-=1

            else:
                nums1[cur] = nums2[n]
                n-=1
            cur-=1

        while (m>-1):
            nums1[cur] = nums1[m]
            m-=1
            cur-=1

        while (n>-1):
            nums1[cur] = nums2[n]
            n-=1
            cur-=1

        return nums1


        