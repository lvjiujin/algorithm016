#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 方法一：经典的递归
        # res = list()
        # self.postorder(root,res)
        # return res
        # 方法二：用栈来模拟,反向输出
        # stack, output = [root,], []
        # while stack:
        #     root = stack.pop()
        #     output.append(root.val)
        #     if root.left:
        #         stack.append(root.left)
        #     if root.right:
        #         stack.append(root.right)
        # return output[::-1]
        # 方法三：用栈来模拟真正的后序遍历
        if not root:
            return []
        stack, output = [(0, root)], []
        while stack:
            flag, node = stack.pop()
            if not node:
                continue
            if flag == 1:
                output.append(node.val)
            else:
                stack.append((1, node))
                stack.append((0, node.right))
                stack.append((0, node.left))
        
        return output

    def postorder(self, root, res):
        if not root:
            return
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)
# @lc code=end

