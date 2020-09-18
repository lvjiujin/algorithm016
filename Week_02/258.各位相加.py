#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # 递归:
        # if num <10:
        #     return num
        # sum = 0
        # while num != 0:
        #     sum += num%10
        #     num //=10
        # return self.addDigits(sum)
        # 迭代:
        # while num >=10:
        #     sum = 0
        #     while num !=0:
        #         sum += num %10 
        #         num //=10
        #     num = sum
        
        # return num
        # 数根:
        # https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
        # https://leetcode.com/problems/add-digits/discuss/68580/Accepted-C%2B%2B-O(1)-time-O(1)-space-1-Line-Solution-with-Detail-Explanations
        # https://leetcode-cn.com/problems/add-digits/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-5-7/
        if num == 0:
            return 0
        return (num - 1) % 9 + 1;


# @lc code=end

