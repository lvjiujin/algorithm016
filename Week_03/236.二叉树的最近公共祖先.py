#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 参考链接:
        # https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
        # https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-lowest-common-ancestor-of-a-binary-tree-er-cha/
        # if not root or root == q or root == p:
        #     return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if not left:
        #     return right
        # if not right:
        #     return left
        
        # return root
        # 上述代码的简化版：来自光头哥的代码：
        # if root in (None, p, q): return root
        # left, right = (self.lowestCommonAncestor(kid, p, q)
        #             for kid in (root.left, root.right))
        # return root if left and right else left or right
        #  第二种方法：递归 + 剪枝 算法
        isFind = False
        def search(node) : 
            nonlocal isFind
            # 分析点 1
            if not node:
                return None
            # 分析点 2
            if node == p or node == q:
                #  如果当前点就是其中一个目标点，子树被剪枝
                return node
        
            # 分析点 3
            leftResult = search(node.left)

            if isFind:
                # 左边已经找到了，右边被剪枝
                return leftResult
            # 分析点 4
            rightResult = search(node.right)

            if leftResult and rightResult:
       
                # 左右都找到了，说明现在是最近父祖先
                isFind = True
                return node
            # 分析点 5
            return leftResult if leftResult  else rightResult
        

        return search(root)

        
# @lc code=end

