#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) <3:
            return []
        
        result, N = [], len(nums)
        nums.sort()
        
        for i in range(N-1):
            if nums[i] > 0:
                break
            target = - nums[i]
            # convert 3sum to 2sum problem
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, N-1
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
        
        return result
        
# @lc code=end

