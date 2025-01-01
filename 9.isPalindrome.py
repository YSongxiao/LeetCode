class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        stack = []
        if len(x_str) < 2:
            return True
        for i in range(len(x_str) // 2):
            stack.append(x_str[i])
        if len(x_str) % 2 == 0:
            for i in range(len(x_str) // 2, len(x_str)):
                if stack.pop() != x_str[i]:
                    return False
                else:
                    continue
        else:
            for i in range(len(x_str) // 2+1, len(x_str)):
                if stack.pop() != x_str[i]:
                    return False
                else:
                    continue
        return True

solution = Solution()
x = 121
print(solution.isPalindrome(x))
