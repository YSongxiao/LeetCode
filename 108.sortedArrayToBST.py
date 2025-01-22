from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        length = len(nums)
        if length == 1:
            return TreeNode(nums[0])
        elif length == 0:
            return None
        root = TreeNode(nums[length // 2])
        # left tree
        root.left = self.sortedArrayToBST(nums[:length // 2])
        # right tree
        root.right = self.sortedArrayToBST(nums[length // 2 + 1:])
        return root


    # def update(self, root, node):
    #     if node.val > root.val:
    #         if root.right is None:
    #             root.right = node
    #         else:
    #             self.update(root.right, node)
    #     elif node.val < root.val:
    #         if root.left is None:
    #             root.left = node
    #         else:
    #             self.update(root.left, node)


sol = Solution()
nums = [-10, -3, 0, 5, 9]
# nums = [1, 3]
# nums = [0, 1, 2, 3, 4, 5]
root = sol.sortedArrayToBST(nums)
print(sol.sortedArrayToBST(nums))