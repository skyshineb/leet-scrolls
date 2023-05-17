from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i in range(len(arr) - 1, -1, -1):
            cur = arr[i]
            arr[i] = max
            max = cur if max < cur else max
        return arr

if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceElements([17,18,5,4,6,1]))