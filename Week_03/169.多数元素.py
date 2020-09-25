#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 调用系统函数
        # from collections import Counter
        # d = Counter(nums)
        # return d.most_common(1)[0][0]
        
        # 方法二：sort
        nums.sort()
        return nums[len(nums)//2 ]
        # Boyer-Moore Majority vote (摩尔投票法)
        # https://leetcode-cn.com/problems/majority-element/solution/duo-shu-yuan-su-by-leetcode-solution/
        
        # 时间复杂度：O(n)O(n)。Boyer-Moore 算法只对数组进行了一次遍历。
        # 空间复杂度：O(1)O(1)。Boyer-Moore 算法只需要常数级别的额外空间
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


# @lc code=end

