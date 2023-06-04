class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['[', '(', '{']:
                stack.append(c)
                continue
            if len(stack) == 0:
                return False
            t = stack.pop()
            if (t == '(' and c == ')') \
                    or (t == '[' and c == ']') \
                    or (t == '{' and c == '}'):
                continue
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("()"))