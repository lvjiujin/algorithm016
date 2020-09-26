#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 感觉本题目看着简单，分析起来好费劲呀。
        # 给出官方链接，慢慢品吧。递归+动态规划
        '''
        状态 a：root 必须放置摄像头的情况下，覆盖整棵树需要的摄像头数目。
        状态 b：覆盖整棵树需要的摄像头数目，无论root 是否放置摄像头。
        状态 c：覆盖两棵子树需要的摄像头数目，无论节点 root 本身是否被监控到
        根据定义一定有：a>=b>=c
        '''
        # https://leetcode-cn.com/problems/binary-tree-cameras/solution/jian-kong-er-cha-shu-by-leetcode-solution/
        def dfs(root: TreeNode) -> List[int]:
            if not root:
                return [float("inf"), 0, 0]
            
            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return [a, b, c]
        
        a, b, c = dfs(root)
        return b

        
# @lc code=end

