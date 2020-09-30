#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 迭代法， 先判断相等的情况，再判断为None的情况，这样更快些
        # if not root:
        #     return None
        # while root:
        #     if root.val == val:
        #         return root
        #     elif val < root.val:
        #         if not root.left:
        #             return None
                   
        #         else:
        #             root = root.left
        #     else:
        #         if not root.right:
        #             return None
        #         else:
        #             root = root.right
            
        # return None

        # 递归方法
        # 首先确定递归的终止条件
        if not root or val == root.val:
            return root
        # 确定单层递归的逻辑
        if val < root.val:
            root = self.searchBST(root.left, val)
        else:
            root = self.searchBST(root.right,val)
        return root
        
# @lc code=end

