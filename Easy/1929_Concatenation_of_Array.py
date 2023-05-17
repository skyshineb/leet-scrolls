from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [nums[x % len(nums)] for x in range(0, len(nums) * 2)]