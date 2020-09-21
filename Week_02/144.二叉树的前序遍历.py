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
       # 方法一：直接套用pre-order 递归的模板
        # res = list()
        # self.preorder(root,res)
        # return res
        # 方法二：用栈来模拟前序遍历 （DFS）
        # 先将右节点入栈，再将左节点入栈，这样保证出栈的顺序是先左后右。
        # 时间复杂度 O(n),访问每个节点恰好一次， 空间复杂度最坏情况下是整棵树O(n)
        if not root:
            return []

        stack, output = [root,],[]
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return output
        # 方法三：莫里斯遍历:
            # pass
    def preorder(self, root, res):
        if not root:
            return 
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)
# @lc code=end

