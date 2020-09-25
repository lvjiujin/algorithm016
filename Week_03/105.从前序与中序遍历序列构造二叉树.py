#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# from typing import List
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        # 这个非常简洁，比官方好太多了。
        def recur_func(inorder):
            x = preorder.pop(0)  # 每次取前序列表最左端的元素
            node = TreeNode(x)  # 用该元素生成一个node
            idx = inorder.index(x)  # 找到该元素在中序列表中的索引
            left_l = inorder[:idx]  # 用该元素分割中序列表
            right_l = inorder[idx+1:]
            node.left = recur_func(left_l) if left_l else None  
            node.right = recur_func(right_l) if right_l else None
            # 一直探索到最底层的最左端的叶子，然后从下往上一层层返回
            return node

        if not preorder or not inorder: 
            return None  # 判空
        
        return recur_func(inorder)
    

# @lc code=end

