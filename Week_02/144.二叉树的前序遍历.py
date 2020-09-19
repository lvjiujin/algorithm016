#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        self.preorder(root,res)
        return res
    def preorder(self, root, res):
        if not root:
            return 
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)
# @lc code=end

