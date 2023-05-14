class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        net = set()
        prev_size = len(net)
        for i in nums:
            net.add(i)
            size = len(net)
            if size == prev_size:
                return True
            prev_size = size
        return False
