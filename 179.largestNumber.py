from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        import functools
        def new_cmp(a, b):
            if (a+b) > (b+a):
                return 1
            elif (a+b) < (b+a):
                return -1
            else:
                return 0
        res = ""
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        nums_ = sorted(nums, reverse=True, key=functools.cmp_to_key(new_cmp))
        for num in nums_:
            res += num
        while res[0] == "0" and len(res) > 1:
            res = res[1:]
        return res

sol = Solution()
# nums = [3,30,34,5,9]
nums = [34323, 3432]
nums = [0, 0]
print(sol.largestNumber(nums))