class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0

            # Recursively get the max path sum of left and right subtrees
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            # Calculate the max path sum that passes through the current node
            current_max = node.val + left_max + right_max

            # Update the global maximum path sum
            self.global_max = max(self.global_max, current_max)

            # Return the maximum sum of paths that can be extended to the parent
            return node.val + max(left_max, right_max)

        self.global_max = float('-inf')
        dfs(root)
        return self.global_max