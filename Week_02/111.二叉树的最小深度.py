#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 方法一
        """
        这道题的关键是搞清楚递归结束条件

        叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
        当 root 节点左右孩子都为空时，返回 1
        当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
        当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值
        """
        # if not root: 
        #     return 0
        # d = list(map(self.minDepth, (root.left, root.right))) if root else [-1]
        # return 1 + (min(d) or max(d))
        # 方法二：递归法：深度优先
        """
        最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

        说明: 叶子节点是指没有子节点的节点。
        递归法
        节点不存在时，返回0
        左右子节点均不存在时，说明该节点为叶子节点，返回1
        左右子节点存在一个时，返回1+minDepth(子节点)
        左右子节点均存在时，返回1+较小的minDepth(子节点)

        """
        
        # if not root: 
        #     return 0
        # l, r = self.minDepth(root.left), self.minDepth(root.right)
        # # 左右孩子都不为空，返回最小深度+1即可
        # if root.left and root.right: 
        #     return 1 + min(l, r)
        # else:
        #     return 1 + l + r
            # 这里其中一个节点为空，说明m1和m2有一个必然为0，所以可以返回l + r + 1;
        
        # 方法三：广度优先：BFS
        # 当我们找到一个叶子节点时，直接返回这个叶子节点的深度。
        # 广度优先搜索的性质保证了最先搜索到的叶子节点的深度一定最小
        # 时间复杂度，O(n)，因为每个节点访问一次 其实就类似于一个前序遍历
        if not root:
            return 0
        from collections import deque
        que = deque([(root, 1)])
        while que:
            # print("que = ", que)
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))

        return 0


    


        


# @lc code=end

