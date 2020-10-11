#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy 
        if not nums:
            return False
        L = len(nums)
        dis = 0
        for i in range(0, L):
            if i <= dis:
                # 最远可以到达的位置不会被更新；
                # i + nums[i] 代表本次最远可以到达的位置，只要不大于等于截止目前位置最远可以到达的位置，那就不会被更新。
                dis = max(dis, i + nums[i])
                # L - 1 因为实际上我们最低需要的步数就是L-1, 因为一个元素的时候，不需要动，两个元素的话，一步就够了。
                if dis >= L-1:
                    return True
        
        return False
# @lc code=end

