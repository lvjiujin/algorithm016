#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 通过本题目，下次有多重方法时直接通过函数内部的不同函数名来区分，不要注释掉了，否则后面提交到github上看不清晰。
        # 参考链接：https://leetcode-cn.com/problems/combinations/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-ma-/
        # 方法一：没有剪枝操作
        def dfs(n, k, begin, path,  res):
            # 终止递归的条件是:path 的长度等于k
            if len(path) == k:
                res.append(path[:])
                return
            
            # 遍历可能的搜索起点
            for i in range(begin, n+1):
                # 向路径中添加一个数
                path.append(i)
                # 下一轮搜索，设置的搜索起点要加1，因为组合数不允许出现重复元素。
                # print(" recursion before => " ,path)
                dfs(n, k, i + 1, path, res)
                # print(" recursion after => " , path)
                # 重点理解这里：深度优先遍历有回头的过程：因为递归之前做什么，递归之后做相同的操作。
                path.pop()
        
        # 方法2：backtrack + pruning  回溯 + 剪枝
        def dfs_pruning(n,k, begin, path, res):
            if len(path) == k:
                res.append(path[:])
                return
            # 我们的剪枝过程就是：把 i <= n 改成 i <= n - (k - path.size()) + 1 
            for i in range(begin, n - (k - len(path)) + 1 + 1):
                path.append(i)
                dfs_pruning(n, k, i + 1, path, res)
                path.pop()
        

        res = []
        if k == 0 or n < k:
            return res
        # 从1开始是题目设定的要求
        path = []
        # dfs(n, k, 1, path, res)
        dfs_pruning(n, k, 1, path, res)

        return res
# @lc code=end

