class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        


        l = 0
        r = len(numbers)-1

        while l < r:
            sum2 = numbers[l] + numbers[r]
            if target < sum2:
                r -=1

            elif target > sum2:
                l +=1

            else:
                return [l+1,r+1]