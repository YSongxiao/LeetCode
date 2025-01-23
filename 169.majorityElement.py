from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)
        if len(nums) == 1:
            return nums[0]
        times = {}
        for num in nums:
            if num in times:
                times[num] += 1
                if times[num] > len(nums) // 2:
                    return num
            else:
                times[num] = 1


solu = Solution()
nums = [3, 2, 3]
print(solu.majorityElement(nums))