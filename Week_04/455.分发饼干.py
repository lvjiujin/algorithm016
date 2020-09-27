#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 这种贪心方法的证明:https://leetcode-cn.com/problems/assign-cookies/solution/tan-xin-jie-fa-by-cyc2018/
        g.sort()
        s.sort()
        i = j = count = 0
        while i < len(g) and j < len(s):
            if g[i]<=s[j]:
                # 如果从小到大排序，那么当一块饼干满足一个小孩后，小孩加一。不满足的话，饼干加一（扩大饼干）
                # 如果从大到小排序，那么当一块饼干满足一个小孩后，饼干加一。不满足的话，小孩加一。（减小孩子期望）
                i+=1
                count+=1
            j+=1
        return count
        
# @lc code=end

