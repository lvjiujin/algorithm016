#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
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
    def postorder(self, root: 'Node') -> List[int]:
        # 方法1 递归:
        if not root:
            return []
        res = list()
        for child in root.children:
            res.extend(self.postorder(child))
            
        res.append(root.val)
        return res

# @lc code=end

