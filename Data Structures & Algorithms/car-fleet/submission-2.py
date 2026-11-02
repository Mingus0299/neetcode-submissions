class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        lst = [(p,s) for p,s in zip(position, speed)]
        stack = []
        lst.sort(reverse = True)

        for p, s in lst:
            time = (target-p)/s
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)

        return len(stack)