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
        # 递归： 这个思路很难懂。
        # res = []
        # n = len(nums)
        
        # def helper(i, tmp):
        #     print("tmp = ", tmp)
        #     res.append(tmp)
        #     print("i = ", i)
        #     for j in range(i, n):
        #         print("j = ", j)
        #         print("nums[{}] = {}".format(j, nums[j]))
        #         helper(j + 1,tmp + [nums[j]] )
        # helper(0, [])
        # return res 
        # 回溯:
        res = []
        # 我们用指针index描述一个节点的状态，即当前递归考察的数字 nums[index]
        def backtrack(index, path):
            # 指针越界，加入解集，结束当前的递归。
            if index == len(nums):
                res.append(path[:])
                return
            # 选择这个元素
            path.append(nums[index])
            backtrack(index + 1, path) # 往下递归
            path.pop() # 递归结束，撤销选择
            backtrack(index + 1, path) # 不选这个元素，往下递归
        backtrack(0, [])
        return res


def main():
    mysolu = Solution()
    nums = [1,2,3]
    res = mysolu.subsets(nums)
    print("res = ", res)

if __name__ == '__main__':
    main()
# @lc code=end

