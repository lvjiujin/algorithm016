#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 方法一：观察结果，充分利用Python的切片功能
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k] 

        # k = k % len(nums)
        # if not k:
        #     return
        # nums[:k], nums[k:] = nums[-k:], nums[:-k]
      

        # 递归的这种方法，占用空间最小
        # 三次反转
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # 第一次整体反转
        reverse(nums, 0, end)
        # 第二次反转前k个数
        reverse(nums, 0, k-1)
        # 第三次反转后面的部分
        reverse(nums,k, end)
        
        
 
           
        




    
# @lc code=end

