#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        self.inorder(root, res)
        return res
    def inorder(self,root, res):
        if not root :
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

# @lc code=end

