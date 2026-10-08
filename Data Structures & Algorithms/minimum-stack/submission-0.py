class MinStack:

    #[3,5,2,6,7]
    #[3,5,5,6,7]

    def __init__(self):
        self.stack = []
        self.max_ls = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        curr_max = min(self.max_ls[-1] if self.max_ls else val, val)
        self.max_ls.append(curr_max)

    def pop(self) -> None:
        val = self.stack.pop()
        self.max_ls.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.max_ls[-1]
        
