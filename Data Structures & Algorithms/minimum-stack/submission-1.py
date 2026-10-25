class MinStack:

    def __init__(self):
        self.stack = []
        self.min_s = []
        

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_s:
            val = min(val, self.min_s[-1])
        self.min_s.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_s.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_s[-1]
        
