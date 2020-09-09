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
        # N = len(nums)
        # for j in range(k):
        #     for i in range(N-1,0,-1):
        #         temp = nums[i]
        #         nums[i] = nums[i-1]
        #         nums[i-1] = temp
   
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k] 

        # k = k % len(nums)
        # if not k:
        #     return
        # nums[:k], nums[k:] = nums[-k:], nums[:-k]
      
        # n = len(nums)
        # k = k % n
        # # if not k:
        # #     return 
        # nums[:] = nums[n-k:] + nums[:n-k]

        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
           
        




    
# @lc code=end

