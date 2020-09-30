#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 方法一：递归法 （比较快）
        # if not root:
        #     return 0
        # else:
        #     left_max = self.maxDepth(root.left)
        #     right_max = self.maxDepth(root.right)
        #     return max(left_max, right_max) + 1
        # 方法二：广度优先 BFS （层序遍历，相当于套用模板) 比较慢
        # if not root:
        #     return 0
        # depth = 0
        # queue = [root]
        # while queue:
        #     size  = len(queue)
        #     depth += 1
        #     for _ in range(size):
        #         node = queue.pop(0)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
            
        # return depth
        # 方法三：深度优先 DFS 迭代法
        depth = 0
        stack = [(root,1)]
        
        while stack:
            root,leng=stack.pop()
            if not root:
                return 0
            
            if leng > depth:
                depth = leng            
            # 注意：这里一定要是先右后左的顺序入栈，这样出栈的顺序才符合先左子树，后右子树。
            # 每深入一层root.right 或root.left, length就加一。
            if root.right:
                stack.append((root.right,leng+1))
            if root.left:
                stack.append((root.left,leng+1)) 
                
        return depth
        
        
# @lc code=end

