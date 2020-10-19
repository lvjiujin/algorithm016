#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        # 贪心法
        '''
        在遍历数组时，我们不访问最后一个元素，这是因为在访问最后一个元素之前，我们的边界一定大于等于最后一个位置，
        否则就无法跳到最后一个位置了。如果访问最后一个元素，
        在边界正好为最后一个位置的情况下，我们会增加一次「不必要的跳跃次数」，因此我们不必访问最后一个元素。
        '''
        max_pos, pre_max_pos, L, step  = 0, 0, len(nums), 0
        # max_pos: 当前能够到达的最远位置
        # pre_max_pos 前一个能够达到的最原位置，
        # 如果遍历到了此位置，则说明需要下一跳，已到达更远位置
        # step 跳跃次数
        for i in range(L-1):
            
            if max_pos >= i: # 如果当前位置可以到达
                # 更新到最远能够到达的位置
                max_pos = max(max_pos, nums[i] + i)
                # 如果当前位置为上一个可以到达的最远位置，则需要下一跳来到达更远处，即增加步数
                if pre_max_pos == i:
                    pre_max_pos = max_pos
                    step += 1
        return step


# @lc code=end

