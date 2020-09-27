#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # two travel 
        # if not root:
        #     return None
        # def find_path(root, target):
        #     node = root
        #     path = []
        #     while node != target:
        #         path.append(node)
        #         if target.val > node.val:
        #             node = node.right
        #         else:
        #             node = node.left
        #     path.append(node)
        #     return path
        
        # path_p = find_path(root,p)
        # path_q = find_path(root,q)
        # ancestor = None
        # for u, v in zip(path_p, path_q):
        #     if u == v:
        #         ancestor = u
        #     else:
        #         break
        # return ancestor
        # one travel 
        # 当前节点大于 p,q时，说明要往左寻找，小于p,q时要往右寻找，否则就是找到了。
        if not root:
            return None
        node = root
        while True:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                break
        return node
            


        
# @lc code=end

