#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 方法一
        if not root: 
            return 0
        d = list(map(self.minDepth, (root.left, root.right))) if root else [-1]
        return 1 + (min(d) or max(d))


# @lc code=end

