from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = {}
        ans = []
        for i in range(len(s) - 9):
            if s[i: i+10] in res:
                res[s[i: i+10]] += 1
            else:
                res[s[i: i+10]] = 1
        for key in res.keys():
            if res[key] > 1:
                ans.append(key)
        return ans


sol = Solution()
s = "AAAAAAAAAAA"
print(sol.findRepeatedDnaSequences(s))
