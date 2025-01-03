class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1

solution = Solution()
haystack = "leetcode"  # "sadbutsad"
needle = "leeto" # "sad"
print(solution.strStr(haystack, needle))


