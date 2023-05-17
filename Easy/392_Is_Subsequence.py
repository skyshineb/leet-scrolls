class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si, ti = 0, 0
        while si < len(s) and ti < len(t):
            cs = s[si]
            ct = t[ti]
            if cs == ct:
                si += 1
                ti += 1
            else:
                ti += 1
        if si == len(s):
            return True
        return False

