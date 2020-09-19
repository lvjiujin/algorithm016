#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        # 方法1 递归:
        if not root:
            return []
        res = list()
        res.append(root.val)
        for child in root.children:
            res.extend(self.preorder(child))
            
        
        return res
        
# @lc code=end

