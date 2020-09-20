#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 方法一，利用系统函数。Counter操作，应该是O（1），most_common不清楚。
        # from collections import Counter
        # x = Counter(nums)
        # return [v[0] for v in x.most_common(k)]
        # heap + Counter
        import heapq
        from collections import Counter
        res = []
        dic = Counter(nums)
        max_heap = [(-val, key) for key, val in dic.items()]
        heapq.heapify(max_heap)
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res   

# @lc code=end

