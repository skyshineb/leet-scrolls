from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def rec_gen(out, stack, open, max):
            if open < max:
                rec_gen(out + '(', stack.copy() + ['('], open + 1, max)
                if len(stack) != 0:
                    cp = stack.copy()
                    cp.pop()
                    rec_gen(out + ')', cp, open, max)

            else:
                while len(stack) != 0:
                    out = out + ')'
                    stack.pop()
                res.append(out)

        rec_gen("", [], 0, n)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))