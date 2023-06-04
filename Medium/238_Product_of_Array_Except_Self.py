from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        prefix = 1
        for i in range(0, len(nums) - 1):
            prefix = prefix * nums[i]
            output.append(prefix)
        postfix = 1
        for i in range(len(nums) - 1, 0, -1):
            postfix = postfix * nums[i]
            output[i - 1] = output[i - 1] * postfix
        return output


if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))