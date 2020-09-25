'''
Author: your name
Date: 2020-09-24 12:32:06
LastEditTime: 2020-09-25 14:23:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Week_03\106.从中序与后序遍历序列构造二叉树.py
'''
#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            # 如果这里没有节点构造二叉树了，就结束
            if in_left > in_right:
                return None
            
            # 选择 post_idx 位置的元素作为当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 根据 root 所在位置分成左右两棵子树
            index = idx_map[val]
 
            # 构造右子树, 注意这里的顺序，一定是先构建右子树，再构建左子树
            root.right = helper(index + 1, in_right)
            # 构造左子树
            root.left = helper(in_left, index - 1)
            return root
        
        # 建立（元素，下标）键值对的哈希表
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)


# @lc code=end

