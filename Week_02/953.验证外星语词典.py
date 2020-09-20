#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # if not words:
        #     return False
        # d = {x:y for x in order for y in range(len(order))}
        # for x in words:
        #     for i in range(len(x) -1):
        #         if d[x[i]] > d[x[i+1]]:
        #             return False
        # return True
        order_map = {j:i  for i,j in enumerate(order)}

        for i in range(len(words)-1):
            if self.compare(words[i],words[i+1],order_map):
                return False
        return True
        
    def compare(self,x,y,order_map):
        for i in range(len(x)):
            # i > len(y) 说明x的长度比y长，而且len(y)的长度都相同
            if i>=len(y):
                return True
            if order_map[x[i]]>order_map[y[i]]:
                return True
            if order_map[x[i]]<order_map[y[i]]:
                return False
        return False

# @lc code=end

