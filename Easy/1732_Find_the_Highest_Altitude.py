from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        current = 0
        for g in gain:
            current = current + g
            if highest < current:
                highest = current
        return highest