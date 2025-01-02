from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        prefixs = [""]
        for digit in digits:
            tmp_prefix = []
            for prefix in prefixs:
                for letter in dict[digit]:
                    tmp_prefix.append(prefix + letter)
            prefixs = tmp_prefix
        if prefixs == [""]:
            return []
        return prefixs


solution = Solution()
digits = ""
result = solution.letterCombinations(digits)
print(result)