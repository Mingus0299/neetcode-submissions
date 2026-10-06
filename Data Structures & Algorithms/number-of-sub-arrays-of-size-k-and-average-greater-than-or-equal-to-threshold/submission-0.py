class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

# sliding windows: two points : left, right
        left = 0
        right = k-1
        answer = 0

        total = 0
        for i in range( k-1):
            total += arr[i]

        

        while(right < len(arr)):
            total += arr[right]
            if (total/k >= threshold):
                answer+=1
            total -= arr[left]
            left+=1
            right+=1

        return answer