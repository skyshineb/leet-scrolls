from typing import List

 # My mind is dazed rn, this solution is not working
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = list(ord(strs[0][x]) for x in range(0, len(strs[0])))
        length = 0
        for i in range(1, len(strs)):
            istr = strs[i]
            for j in range(0, min(len(istr), len(res))):
                if res[j] ^ ord(istr[j]) == 0:
                    if length < j + 1:
                        length = j
                else:
                    break
            res = list(ord(istr[x]) for x in range(0, len(istr)))

        if length > 0:
            return strs[0][0:length - 1]
        else:
            return ""


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(["ab", "a"]))