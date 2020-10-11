#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        from collections import defaultdict, Counter
        
        # 就是这个哈希表的默认值是当前哈希表中元素的个数，
        # 这样每个 key 对应的 value 就会是 0, 1, 2, ... 这样，不会有重复。UID 就是要不能重复
        trees = defaultdict()
        counter = Counter()
        trees.default_factory = trees.__len__
        ans = []
        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                counter[uid] +=1
                if counter[uid] == 2:
                    ans.append(node)
                return uid
        
        lookup(root)
        return ans
 
# @lc code=end

