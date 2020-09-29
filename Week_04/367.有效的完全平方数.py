#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 这种思路非常奇特:
        # return num ** 0.5 %1 == 0
        # 利用完全平方根的性质:
        '''
        完全平方数可以通过累加从1往后的奇数找到，
        时间复杂度 O(n)
        1 = 1;
        4 = 1 + 3;
        9 = 1 + 3 + 5;
        16 = 1 + 3 + 5 + 7;
        '''
        # if num == 0:
        #     return False
        
        # i = 1
        # while num > 0:
        #     num -= i
        #     i += 2
        # return num == 0
        # 利用牛顿迭代法： TS O(logN)
        # if num == 1:
        #     return True
        # r = num
        # while r > num //r:
        #     r = (r + num//r )//2
        # return r*r == num
        # 二分查找法:
        if num == 1:
            return True
        left, right = 2, num//2
        while left <= right:
            mid = (left + right)>>1
            guess_square = mid * mid
            if guess_square == num:
                return True
            elif guess_square > num:
                right = mid-1
            else:
                left = mid+1
            
        print("left = ", left)
        return False

   
# @lc code=end

