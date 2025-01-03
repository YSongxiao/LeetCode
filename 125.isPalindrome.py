class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isDigitAlpha(s):
            return s.isalpha() or s.isdigit()
        N = len(s)
        start = 0
        end = N - 1
        while start <= end:
            if isDigitAlpha(s[start]) and isDigitAlpha(s[end]):
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1
            elif not isDigitAlpha(s[start]):
                start += 1
            elif not isDigitAlpha(s[end]):
                end -= 1
        return True


solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))