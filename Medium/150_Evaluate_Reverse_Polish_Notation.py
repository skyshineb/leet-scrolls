from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']
        for t in tokens:
            if t not in operations:
                stack = [int(t)] + stack
            elif t == '+':
                stack = [stack.pop(1) + stack.pop(0)] + stack
            elif t == '-':
                stack = [stack.pop(1) - stack.pop(0)] + stack
            elif t == '*':
                stack = [stack.pop(1) * stack.pop(0)] + stack
            elif t == '/':
                stack = [int(stack.pop(1) / stack.pop(0))] + stack
        return stack.pop()

#Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#= ((10 * (6 / (12 * -11))) + 17) + 5
#= ((10 * (6 / -132)) + 17) + 5
#= ((10 * 0) + 17) + 5
#= (0 + 17) + 5
#= 17 + 5
#= 22
if __name__ == '__main__':
    sol = Solution()
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))