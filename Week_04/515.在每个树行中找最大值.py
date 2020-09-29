#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # 主要思想就是BFS, 和二叉树的层序遍历非常类似。
        if not root:
            return []
        res, queue = [], [root]
        while queue:
            size = len(queue)
            res_max = float('-inf')
            for _ in range(size):
                node = queue.pop(0)
                value = node.val
                if value > res_max:
                    res_max = value
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(res_max)
        return res 
# @lc code=end

