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
        nums.sort()
        result, N = [], len(nums)

        for i in range(N-1):
            target = - nums[i]
            # convert 3sum to 2sum problem
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s, e = i + 1, N-1
            while s < e:
                if nums[s] + nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s += 1
                    e -= 1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1
                    while s < e and nums[e] == nums[e+1]:
                        e -= 1
                elif nums[s] + nums[e] < target:
                    s += 1
                elif nums[s] + nums[e] > target:
                    e -= 1
        
        return result
        # 不是很明白，为何下面的做法比上面的快很多。
        # nums.sort()
        # N, result = len(nums), []
        # for i in range(N):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     target = nums[i]*-1
        #     s,e = i+1, N-1
        #     while s<e:
        #         if nums[s]+nums[e] == target:
        #             result.append([nums[i], nums[s], nums[e]])
        #             s = s+1
        #             while s<e and nums[s] == nums[s-1]:
        #                 s = s+1
        #         elif nums[s] + nums[e] < target:
        #             s = s+1
        #         else:
        #             e = e-1
        # return result
# @lc code=end

