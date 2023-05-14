from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, x in enumerate(nums):
            for idx2, y in enumerate(nums[idx1 + 1:]):
                if target - x - y == 0:
                    return [idx1, idx2 + idx1 + 1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([3,2,4], 6))