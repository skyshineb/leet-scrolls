class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        m1 = dict()
        for c in s:
            valC = m1.get(c)
            cnt = 0 if valC is None else valC
            m1[c] = cnt + 1
        for c in t:
            valC = m1.get(c)
            if valC is None:
                return False
            if valC == 1:
                m1.pop(c)
            else:
                m1[c] = valC - 1
        return len(m1) == 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram("anagram", "nagram"))
