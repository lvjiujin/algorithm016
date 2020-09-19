#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # 方法一：递归法
        if not root:
            return 0
        else:
            child_max = 0
            if root.children:
                for child in root.children:
                    child_depth = self.maxDepth(child)
                    if child_depth > child_max:
                        child_max = child_depth
            return child_max + 1
        # DFS
        # BFS
        
# @lc code=end

