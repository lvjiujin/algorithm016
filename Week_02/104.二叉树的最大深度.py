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
        # 方法一：递归法
        # if not root:
        #     return 0
        # else:
        #     left_max = self.maxDepth(root.left)
        #     right_max = self.maxDepth(root.right)
        #     return max(left_max, right_max) + 1
        # 方法二：广度优先 BFS
        # depth = 0
        # level = [root] if root else []
        # while level:
        #     depth += 1
        #     queue = []
        #     for el in level:
        #         if el.left:
        #             queue.append(el.left)
        #         if el.right:
        #             queue.append(el.right)
            
        #     level = queue

        # return depth
        # 方法三：广度优先 DFS
        depth = 0
        stack = [(root,1)]
        
        while stack:
            root,leng=stack.pop()
            if not root:
                return 0
            
            if leng > depth:
                depth = leng            
            
            if root.right:
                stack.append((root.right,leng+1))
            if root.left:
                stack.append((root.left,leng+1)) 
                
        return depth
        
        
# @lc code=end

