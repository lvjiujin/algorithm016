#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # 该题目和530.二叉搜索树的最小绝对差 一模一样,练手过遍数
        res = []
        
        def inorder(node, res):
            if not node:
                return 
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
        inorder(root, res)
        min_val = float('inf')
        L = len(res)
        for i in range(L-1, 0, -1):
            min_val = min(min_val, abs(res[i] - res[i-1]))
        return min_val
        
# @lc code=end

