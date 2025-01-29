class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        diction = {}
        reverse_dict = {}
        if len(pattern) != len(s):
            return False
        for num, pat in enumerate(pattern):
            if pat not in diction:
                if s[num] in reverse_dict:
                    return False
                else:
                    diction[pat] = s[num]
                    reverse_dict[s[num]] = pat
            else:
                if diction[pat] != s[num]:
                    return False
        return True

sol = Solution()
pattern = "abba"
# s = "dog cat cat dog"
# s = "dog cat cat fish"
s = "cat cat cat cat"
# pattern = "a"
# s = "aaaa"
print(sol.wordPattern(pattern, s))