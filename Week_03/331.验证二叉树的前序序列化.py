#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # number of available slots
        slots = 1

        for node in preorder.split(','):
            # one node takes one slot
            slots -= 1
            
            # no more slots available
            if slots < 0:
                return False
            
            # non-empty node creates two children slots
            if node != '#':
                slots += 2
        
        # all slots should be used up
        return slots == 0

        
# @lc code=end

