class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        length = len(words)
        res = ""
        for i in range(length-1, -1, -1):
            if " " not in words[i] and words[i] != "":
                res += words[i]
                res += " "
        return res[:-1]




sol = Solution()
# s = "the sky is blue"
s = "  hello world  "
# s = "a good   example"
print(sol.reverseWords(s))