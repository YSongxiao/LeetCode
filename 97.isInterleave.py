class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.result = False
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == "":
            if s3 == s2:
                return True
            else:
                return False
        elif s2 == "":
            if s3 == s1:
                return True
            else:
                return False
        else:
            self.interleave_s(s1, s2, s3, True)
            self.interleave_s(s1, s2, s3, False)
        return self.result

    def interleave_s(self, s1: str, s2: str, s3: str, switch: bool):
        L1 = len(s1)
        L2 = len(s2)
        L3 = len(s3)
        if L1 + L2 != L3:
            return
        if self.result:
            return
        if switch:  # select s1
            if s1 == "":
                if s3 == s2:
                    self.result = True
                    return
                else:
                    return
            if s1[0] == s3[0]:
                i = 0
                while i < L1 and i < L3 and s1[i] == s3[i]:
                    self.interleave_s(s1[i+1:], s2, s3[i+1:], not switch)
                    i += 1
            else:
                return
        else:
            if s2 == "":
                if s3 == s1:
                    self.result = True
                    return
                else:
                    return
            if s2[0] == s3[0]:
                i = 0
                while i < L2 and i < L3 and s2[i] == s3[i]:
                    self.interleave_s(s1, s2[i + 1:], s3[i + 1:], not switch)
                    i += 1
            else:
                return

    def isInterleave_dp(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == "":
            if s3 == s2:
                return True
            else:
                return False
        elif s2 == "":
            if s3 == s1:
                return True
            else:
                return False
        else:
            dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
            dp[0][0] = True
            for i in range(1, len(s1) + 1):
                dp[i][0] = s1[:i] == s3[:i]
            for i in range(1, len(s2) + 1):
                dp[0][i] = s2[:i] == s3[:i]
            dp[0][1] = s2[0] == s3[0]
            dp[1][0] = s1[0] == s3[0]
            for i in range(1, len(s1) + 1):
                for j in range(1, len(s2) + 1):
                    dp[i][j] = (dp[i][j-1] and s3[i+j-1] == s2[j-1]) or (dp[i-1][j] and s3[i+j-1] == s1[i-1])
            return dp[len(s1)][len(s2)]


solution = Solution()
# s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
# s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
# s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
s1 = "aabcc"
s2 = "dbbca"
# s3 = "aadbbcbcac"
s3 = "aadbbbaccc"
s1 = "db"
s2 = "b"
s3 = "cbb"
print(solution.isInterleave_dp(s1, s2, s3))