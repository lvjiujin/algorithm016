# @before-stub-for-debug-begin
from python3problem66 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
    # def plusOne(self, digits: List[int]) -> List[int]:
        if not digits or len(digits) == 0:
            return []
        # 最高位为0，不合法
        # if digits[0] == 0 and len(digits) > 1:
        #     return []
        # result = list()
        
        # # carry bit problem 
        # carry, N = 0, len(digits)

        # for i in range(N):
        #     if i == 0:
        #         sum = digits[N-1-i] + 1 + carry
        #     else:
        #         sum = digits[N-1-i]  + carry
        #     carry = sum //10
        #     sum = sum %10
        #     result.append(sum)
        # if carry == 1:
        #     result.append(carry)
        # result.reverse()

        # return result
        N = len(digits)
        for i in range(N-1, -1, -1):
            if digits[i] !=9:
                # 低位上的进位通过这里的+1来补偿。补偿后就直接返回。
                digits[i] +=1
                return digits
            else:
                # 某一位为9，直接置位为0，不考虑进位，进位逻辑在上面的if中处理。
                digits[i] = 0
                if digits[0] == 0:
                    digits.insert(0, 1)
                    return digits

# def main():
#     solu = Solution()
#     dig = solu.plusOne([8,0,9,9])
#     print(dig)
# if __name__ == 'main':
#     main()
# @lc code=end

