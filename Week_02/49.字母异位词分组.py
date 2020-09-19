#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 分类计数方法: 很奇妙
        # https://leetcode-cn.com/problems/group-anagrams/solution/zi-mu-yi-wei-ci-fen-zu-by-leetcode/
        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
            print(tuple(count))
        return list(ans.values())
        # 排序方法：
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
            
        # return list(ans.values())




# @lc code=end

