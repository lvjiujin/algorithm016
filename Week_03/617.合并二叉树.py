#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 非常类似于preorder 先序遍历， 当然你也可以说是DFS啦。
        # 递归的优势之处在于代码可以写的非常简洁，复杂交给系统吧。交给计算机吧。
        '''
        时间复杂度：O(min(m,n))，其中 m 和 n 分别是两个二叉树的节点个数。对两个二叉树同时进行深度优先搜索，
        只有当两个二叉树中的对应节点都不为空时才会对该节点进行显性合并操作，因此被访问到的节点数不会超过较小的二叉树的节点数。

        空间复杂度：O(min(m,n))，其中 m 和 n 分别是两个二叉树的节点个数。空间复杂度取决于递归调用的层数，
        递归调用的层数不会超过较小的二叉树的最大高度，最坏情况下，二叉树的高度等于节点数。

        '''
        # if not t1:
        #     return t2
        # if not t2:
        #     return t1
        # mergedNode = TreeNode(t1.val+t2.val)
        # mergedNode.left = self.mergeTrees(t1.left, t2.left)
        # mergedNode.right = self.mergeTrees(t1.right, t2.right)
        
        # return mergedNode

        # 方法二 DFS 中序遍历
        # if not t1:
        #     return t2
        # if not t2:
        #     return t1
        # mergedNode = TreeNode(0)
        # mergedNode.left = self.mergeTrees(t1.left, t2.left)
        # mergedNode.val = t1.val + t2.val
        # mergedNode.right = self.mergeTrees(t1.right, t2.right)
        # return mergedNode
        # 方法三：DFS 后续遍历:
        if not t1:
            return t2
        if not t2:
            return t1
        mergedNode = TreeNode(0)
        mergedNode.right = self.mergeTrees(t1.right, t2.right)
        mergedNode.left = self.mergeTrees(t1.left, t2.left)
        mergedNode.val = t1.val + t2.val
        return mergedNode

        # 方法四 BFS（层序遍历)
        # 想到层序遍历，没有最小重复单元，不能够进行递归，代码老长老长，就开心不起来。不想掌握了，太long了。
        # 优先第一种吧。复杂交给系统吧，交给计算机吧。
        # 参考leetcode 102 题目,二叉树的层序遍历。
        # if not t1:
        #     return t2
        # if not t2:
        #     return t1
        # from collections import deque
        # merged = TreeNode(t1.val + t2.val)
        # queue = deque([merged])
        # queue1 = deque([t1])
        # queue2 = deque([t2])

        # while queue1 and queue2:
        #     node = queue.popleft()
        #     node1 = queue1.popleft()
        #     node2 = queue2.popleft()
        #     left1, right1 = node1.left, node1.right
        #     left2, right2 = node2.left, node2.right
        #     if left1 or left2:
        #         if left1 and left2:
        #             left = TreeNode(left1.val + left2.val)
        #             node.left = left
        #             queue.append(left)
        #             queue1.append(left1)
        #             queue2.append(left2)
        #         elif left1:
        #             node.left = left1
        #         elif left2:
        #             node.left = left2
        #     if right1 or right2:
        #         if right1 and right2:
        #             right = TreeNode(right1.val + right2.val)
        #             node.right = right
        #             queue.append(right)
        #             queue1.append(right1)
        #             queue2.append(right2)
        #         elif right1:
        #             node.right = right1
        #         elif right2:
        #             node.right = right2
        
        # return merged


# @lc code=end

