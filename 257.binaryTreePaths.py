from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.DFS(root, [])
        return self.ans

    def DFS(self, root: Optional[TreeNode], stack):
        stack.append(str(root.val))
        if root.left is not None or root.right is not None:
            if root.left is not None:
                self.DFS(root.left, stack)
            if root.right is not None:
                self.DFS(root.right, stack)
        else:
            res = ""
            for i in range(len(stack)):
                if i != len(stack) - 1:
                    res += stack[i] + "->"
                else:
                    res += stack[i]
            self.ans.append(res)
        stack.pop()




sol = Solution()
root = TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=5)), right=TreeNode(val=3))
print(sol.binaryTreePaths(root))