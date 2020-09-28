#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 和46 类似，做了去重复处理,这个去重逻辑要好好体会。
        # 考虑重复元素一定要优先排序，将重复的都放在一起，便于找到重复元素和剪枝！
        # https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/
        if not nums or len(nums) == 0:
            return []
        def dfs(nums, path, size,  used, res):
            if len(path) == size:
                # 这个地方是个大坑。变量 path 所指向的列表  在深度优先遍历的过程中只有一份 ，深度优先遍历完成以后，回到了根结点，成为空列表。
                # path[:] 是path的一个拷贝：
                res.append(path[:])
                return
            # 在非叶子结点处，产生不同的分支，这一操作的语义是：在还未选择的数中依次选择一个元素作为下一个位置的元素，这显然得通过一个循环实现。
            for i in range(size):
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    # 注意: i > 0 and nums[i] == nums[i - 1] and used[i - 1] 这两种写法相同，但是上面写法效率更高些，相见上面链接
                    continue

                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    # print(" recursion before => " ,path)
                    dfs(nums,  path, size, used, res)
                    # print(" recursion after => " , path)
                    used[i] = False
                    path.pop()
                    # print("path = ", path)

        # 排序是为了后面做避免重复处理的逻辑上更简单
        nums.sort()
        res, path, size = [], [], len(nums)
        used = [False for _ in range(size)]
        dfs(nums, path, size, used, res)
        
        return res
# @lc code=end

