from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for n in nums:
            if n in freq.keys():
                freq[n] = freq[n] + 1
            else:
                freq[n] = 1
        sdict = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        res = list()
        for i in range(0,k):
            res.append(sdict[i][0])
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))