#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # BFS
        if not root:
            return root
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                r = queue.pop(0)
                if i < size - 1:
                    r.next = queue[0]
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
        return root
# @lc code=end

