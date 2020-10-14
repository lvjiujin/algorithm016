#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

# @lc code=start
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        res = None
        from collections import Counter
        for a in A:
            c = Counter(a)
            if res is None:
                res = c
            else:
                res &= c
        return list(res.elements())

    def commonChars2(self, A: List[str]) -> List[str]:
        if not A:
            return []
        res = []
        key = A[0]
        for k in key:
            minimum = min(a.count(k) for a in A)
            res += minimum*k
        return res
                
        
# @lc code=end

