#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 构造字典树
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['#'] = True
        # (i, j) 当前坐标，node当前trie树结点，pre前面的字符串，visited已访问坐标
        def search(i, j, node, pre, visited):
            if '#' in node:
                res.add(pre)
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _i, _j = i + di, j + dj
                # 下标不越界
                if -1 < _i < h and -1 < _j < w and board[_i][_j] in node and (_i, _j) not in visited:
                    search(_i, _j, node[board[_i][_j]], pre+board[_i][_j], visited | {(_i, _j)})
        
        res, h, w = set(), len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:  # 可继续搜索
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})  # dfs搜索
        return list(res)

# @lc code=end

