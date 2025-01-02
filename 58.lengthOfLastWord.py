class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        num = 0
        space_flag = True
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and space_flag:
                continue
            elif s[i] != " " and space_flag:
                space_flag = False
                num += 1
                continue
            elif s[i] != " " and not space_flag:
                num += 1
                continue
            elif s[i] == " " and not space_flag:
                return num
        return num

solution = Solution()
# s = "   fly me   to   the moon  "
s = "Hello World"
print(solution.lengthOfLastWord(s))