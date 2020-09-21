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
        # 方法一递归
        # res = list()
        # self.inorder(root, res)
        # return res
        
        # 方法二，用栈来模拟，下面这种写法确实非常独特，很厉害的写法。
        if not root:
            return []
        cur = root
        stack, output = [],[]
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            output.append(node.val)
            if node.right:
                cur = node.right
        
        return output
    def inorder(self,root, res):
        if not root :
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)


# @lc code=end

