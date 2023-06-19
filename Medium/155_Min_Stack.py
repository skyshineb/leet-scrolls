class MinStack:
    stack = []
    min_stack = []
    len = 0
    def __init__(self):
        pass
    def push(self, val: int) -> None:
        self.stack = [val] + self.stack
        if self.len == 0:
            self.min_stack = [val]
        elif val <= self.min_stack[0]:
            self.min_stack = [val] + self.min_stack
        else:
            self.min_stack = [self.min_stack[0]] + self.min_stack
        self.len = self.len + 1

    def pop(self) -> None:
        self.stack = self.stack[1:]
        self.min_stack = self.min_stack[1:]
        self.len = self.len - 1

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_stack[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()