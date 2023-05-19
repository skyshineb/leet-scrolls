from typing import List

 # My mind is dazed rn, this solution is not working
class Solution:
    def longestCommonPrefix_workingButBad(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = list(ord(strs[0][x]) for x in range(0, len(strs[0])))
        maxInd = 999
        for i in range(1, len(strs)):
            istr = strs[i]
            p = 0
            for j in range(0, min(len(istr), len(res))):
                if res[j] ^ ord(istr[j]) == 0:
                    p += 1
                else:
                    break
            if maxInd > p:
                maxInd = p
                res = list(ord(istr[x]) for x in range(0, len(istr)))

        if maxInd > 0:
            return strs[0][0:maxInd]
        else:
            return ""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        out = strs[0]
        for s in strs[1:]:
            maxI = 0
            for i,c in enumerate(s):
                if i < len(out) and out[i] == c:
                    maxI += 1
                else:
                    break
            out = out[0: maxI]
        return out


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(["cir","car"]))