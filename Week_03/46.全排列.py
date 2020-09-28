#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        # 主要思想回朔法:backtrack
        def dfs(nums,  path, size, used, res):
            if len(path) == size:
                # 这个地方是个大坑。变量 path 所指向的列表 在深度优先遍历的过程中只有一份 ，深度优先遍历完成以后，回到了根结点，成为空列表。
                # path[:] 是path的一个拷贝：
                res.append(path[:])
                return
            # 在非叶子结点处，产生不同的分支，这一操作的语义是：在还未选择的数中依次选择一个元素作为下一个位置的元素，这显然得通过一个循环实现。
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    # print(" recursion before => " ,path)
                    dfs(nums, path, size,  used, res)
                    # print(" recursion after => " , path)
                    # 注意：下面这两行代码发生 「回溯」，回溯发生在从 深层结点 回到 浅层结点 的过程，代码在形式上和递归之前是对称的
                    used[i] = False
                    path.pop()
                    # print("path = ", path)

        res, path, size = [], [], len(nums)
        used = [False for _ in range(size)]
        dfs(nums, path, size, used, res)
        
        return res

# def main():
#     nums = [1,2,3]
#     mysolu = Solution()
#     res = mysolu.permute(nums)
#     print("res = ", res)

# if __name__ == '__main__':
#     main()
# @lc code=end

