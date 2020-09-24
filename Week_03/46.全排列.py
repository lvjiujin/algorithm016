#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 主要思想回朔法:backtrack
        '''
        从 [1, 2, 3] 到 [1, 3, 2] ，深度优先遍历是这样做的，从 [1, 2, 3] 回到 [1, 2] 的时候，需要撤销刚刚已经选择的数 3，
        因为在这一层只有一个数 3 我们已经尝试过了，因此程序回到上一层，需要撤销对 2 的选择，好让后面的程序知道，选择 3 了以后还能够选择 2。

        执行深度优先遍历，从较深层的结点返回到较浅层结点的时候，需要做「状态重置」，即「回到过去」、「恢复现场」
        https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/

        '''
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                # 这个地方是个大坑。变量 path 所指向的列表 在深度优先遍历的过程中只有一份 ，深度优先遍历完成以后，回到了根结点，成为空列表。
                # path[:] 是path的一个拷贝：
                '''
                >>> l1 = [1,2,3]
                >>> id(l1)
                1728591136840
                >>> id(l1[:])
                1728591156424
                '''
                res.append(path[:])
                return
            # 在非叶子结点处，产生不同的分支，这一操作的语义是：在还未选择的数中依次选择一个元素作为下一个位置的元素，这显然得通过一个循环实现。
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    print(" recursion before => " ,path)
                    dfs(nums, size, depth + 1, path, used, res)
                    print(" recursion after => " , path)
                    # 注意：下面这两行代码发生 「回溯」，回溯发生在从 深层结点 回到 浅层结点 的过程，代码在形式上和递归之前是对称的
                    used[i] = False
                    path.pop()
                    print("path = ", path)

        size = len(nums)
        if len(nums) == 0:
            return []
        used = [False for _ in range(size)]
        res = []
        path = []
        dfs(nums, size, 0, path, used, res)
        
        return res

# def main():
#     nums = [1,2,3]
#     mysolu = Solution()
#     res = mysolu.permute(nums)
#     print("res = ", res)

# if __name__ == '__main__':
#     main()
# @lc code=end

