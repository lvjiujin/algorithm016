#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 库函数
        # res = []
        # import itertools
        # for i in range(len(nums) + 1):
        #     for tmp in itertools.combinations(nums,i):
        #         res.append(tmp)
        
        # return res

        # 迭代法：
        # res = [[]]
        # for i in nums:
        #     res = res + [[i] + num for num in res]
        #     # 这个思想和括号生成的思想一样，非常相似。
        #     print("res = ", res)
        
        # return res
        # 递归：回朔法,算是非常简单逻辑的回朔法了。
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res 

# def main():
#     mysolu = Solution()
#     nums = [1,2,3]
#     res = mysolu.subsets(nums)
#     print("res = ", res)

# if __name__ == '__main__':
#     main()
# @lc code=end

