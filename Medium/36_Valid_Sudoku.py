from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            s = set()
            for j in range(0, 9):
                n = board[i][j]
                if n in s:
                    return False
                elif n != '.':
                    s.add(n)

        for i in range(0,9):
            s = set()
            for j in range(0, 9):
                n = board[j][i]
                if n in s:
                    return False
                elif n != '.':
                    s.add(n)

        for p in range(0, 3):
            for k in range(0, 3):
                s = set()
                for i in range(0,3):
                    for j in range(0, 3):
                        n = board[i + p*3][j + k*3]
                        if n in s:
                            return False
                        elif n != '.':
                            s.add(n)
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValidSudoku([[".",".",".","9",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".","3",".",".",".",".",".","1"],[".",".",".",".",".",".",".",".","."],["1",".",".",".",".",".","3",".","."],[".",".",".",".","2",".","6",".","."],[".","9",".",".",".",".",".","7","."],[".",".",".",".",".",".",".",".","."],["8",".",".","8",".",".",".",".","."]]))