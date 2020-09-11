#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 基本思路：就是借助hash表（字典）如果 target - current value 的值在字典中出现过，
        # 那么就是返回相应下标（不考虑多个值的情况，比如两对满足的情况）
        # 不存在将当前值添加到字典中。

        # 另外，因为nums没有说是有序的，所以用双指针并不划算。 
        d1 = dict()
        for i, x in enumerate(nums):
            other = target - x
            if other in d1:
                return [d1[other], i]
            else:
                d1[x] = i
        # 如果找不到如何处理？到底该怎么返回？
        # 返回一个空list，还是返回两个相等的负值。
        return [-1, -1]
        # time complexity O(n)
        # space complexity O(1)
# @lc code=end
        
