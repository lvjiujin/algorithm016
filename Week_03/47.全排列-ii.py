#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 和46 类似，做了去重复处理
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                # 这个地方是个大坑。变量 path 所指向的列表  在深度优先遍历的过程中只有一份 ，深度优先遍历完成以后，回到了根结点，成为空列表。
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
                # 要解决重复问题，我们只要设定一个规则，保证在填第 \textit{idx}idx 个数的时候重复数字只会被填入一次即可。
                # 而在本题解中，我们选择对原数组排序，保证相同的数字都相邻，然后每次填入的数一定是这个数所在重复数集合中
                # 「从左往右第一个未被填过的数字」，即如下的判断条件：
                # https://leetcode-cn.com/problems/permutations-ii/solution/quan-pai-lie-ii-by-leetcode-solution/

                if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
                    continue

                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    # print(" recursion before => " ,path)
                    dfs(nums, size, depth + 1, path, used, res)
                    # print(" recursion after => " , path)
                    # 注意：下面这两行代码发生 「回溯」，回溯发生在从 深层结点 回到 浅层结点 的过程，代码在形式上和递归之前是对称的
                    used[i] = False
                    path.pop()
                    print("path = ", path)

        size = len(nums)
        # 排序是为了后面做避免重复处理的逻辑上更简单
        nums.sort()
        if len(nums) == 0:
            return []
        used = [False for _ in range(size)]
        res = []
        path = []
        dfs(nums, size, 0, path, used, res)
        
        return res
# @lc code=end

