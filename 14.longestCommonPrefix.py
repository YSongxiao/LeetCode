from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N = len(strs)
        prefix = strs[0]
        if N == 0:
            return ""
        else:
            for i in range(1, N):
                tmp_prefix = self.getPrefix(strs[0], strs[i])
                prefix = prefix if prefix < tmp_prefix else tmp_prefix
                if prefix == "":
                    return ""
            return prefix

    def getPrefix(self, str1, str2) -> str:
        N1 = len(str1)
        N2 = len(str2)
        for i in range(min(N1, N2)):
            if str1[i] != str2[i]:
                return str1[:i]
        return str1[:min(N1, N2)]


solution = Solution()
# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["ab", "a"]
print(solution.longestCommonPrefix(strs))