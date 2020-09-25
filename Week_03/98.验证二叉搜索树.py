#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 值得注意的一点是：不仅右子树要大于等于该节点的值，而且整个右子树都要大于等于该节点的值。
        # 不仅左子树要小于等于该节点的值，而且整个左子树都要小于等于该节点的值。
        # 也就是说一个正确的二叉搜索树，它的中序遍历是一个升序序列
        # 方法一：递归:
        # 如果上下界存在，判断当前节点的值是否在界内，如果不在界内，返回false。将当前节点的值作为下界，
        # 继续对node.left 进行递归。将当前节点的值作为下界，继续对node.right进行递归。
        # time complexity:O(n) becuase it requires to check every node in the tree .
        # space complexity: O(n) because the recursion needs the stack space.
        def helper(node, lower = float('-inf'), upper = float('inf')):

            if not node:
                return True
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False
            # 将当前节点的值替换为下界，继续检查右节点的值
            if not helper(node.right,node.val,upper):
                return False
            # 将当前节点的值替换为上界，继续检查左节点的值。
            if not helper(node.left,lower, node.val):
                return False
            
            return True
        return helper(root)
        # 方法二：中序遍历 递归:
        pre = float('-inf')
        def inorder(node):
            nonlocal pre
            if not node:
                return True
            if not inorder(node.left):
                return False
            # 最核心的是这一句，因为中序遍历是一个升序排列，所以要判断当前节点是否大于等于前一个节点
            if node.val <= pre:
                return False
            pre = node.val

            return inorder(node.right)
        
        return inorder(root)

        # 方法三：中序遍历（非递归，stack）
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
        

        
        
# @lc code=end

