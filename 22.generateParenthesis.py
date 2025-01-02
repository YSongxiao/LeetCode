from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.generate("", n, n)
        return self.ans

    def generate(self, string: str, left, right):
        if left == 0 and right == 0:
            self.ans.append(string)
        else:
            if right > left: # left < right
                if left > 0:
                    self.generate(string + "(", left-1, right)
                    self.generate(string + ")", left, right-1)
                else:
                    self.generate(string + ")"*(right - left), left, left)
            elif left == right > 0:
                self.generate(string + "(", left-1, right)


solution = Solution()
n = 1
print(solution.generateParenthesis(n))