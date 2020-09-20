#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # if not root:
        #     return []
        # res = []
        # queue = [root]
        # while queue:
        #     # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
        #     size = len(queue)
        #     tmp = []
        #     # 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
        #     # 如果节点的children子树不为空，也放入队列中
        #     for _ in range(size):
        #         r = queue.pop(0)
        #         tmp.append(r.val)
        #         if r.children:
        #             for ch in r.children:
        #                 queue.append(ch)
            
        #     # 将临时list加入最终返回结果中
        #     res.append(tmp)
        # return res
        # 上面代码的精炼写法：
        q, ret = [root], []
        # any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，是则返回 False，如果有一个为 True，则返回 True。
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret
        
# @lc code=end

