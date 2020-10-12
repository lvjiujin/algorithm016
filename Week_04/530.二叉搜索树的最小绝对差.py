#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from os import get_terminal_size


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 二叉搜索树的中序遍历是一个有序序列。
        res = []
        def inorder(node, res):
            if not node:
                return
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
        inorder(root, res)
        L = len(res)
        min_val = float('inf')
        for i in range(L-1, 0, -1):
            min_val = min(min_val, abs(res[i] - res[i-1]))
        
        return min_val

 
            
# @lc code=end

