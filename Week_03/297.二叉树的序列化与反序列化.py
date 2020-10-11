#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec2:
    # BFS 
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        from collections import deque
        res, queue = [], deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
                
                
            else:
                res.append('X')
        s = ",".join(res)
        # print("s = ", s)
        return s

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        root = TreeNode(data.pop(0))
        queue = [root]
        index, L = 1, len(data)
        while queue:
            node = queue.pop(0)
            if data:
                val = data.pop(0)
                if val != 'X':
                    node.left = TreeNode(val)
                    queue.append(node.left)
            if data:
                val = data.pop(0)
                if val != 'X':
                    node.right = TreeNode(val)
                    queue.append(node.right)

        return root


class Codec:
    # DFS
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'X,'
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + right

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def buildTree(data):
            if not data:
                return None
            val = data.pop(0)
            if val == 'X':
                return None
            node = TreeNode(val)
            node.left = buildTree(data)
            node.right = buildTree(data)
            return node
        data = data.split(",")
        root = buildTree(data)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

