from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        res.append([1])
        res.append([1,1])
        if numRows == 1:
            return [res[0]]
        for i in range(2, numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i-1][j - 1] + res[i-1][j]
            res.append(row)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(5))