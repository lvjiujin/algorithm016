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
        '''
        n = 15 ，k = 4。
        path.size() == 1 的时候，接下来要选择 3 个数，搜索起点最大是 13，最后一个被选的是 [13, 14, 15]；
        path.size() == 2 的时候，接下来要选择 2 个数，搜索起点最大是 14，最后一个被选的是 [14, 15]；
        path.size() == 3 的时候，接下来要选择 1 个数，搜索起点最大是 15，最后一个被选的是 [15]；

        可以归纳出：
        搜索起点的上界 + 接下来要选择的元素个数 - 1 = n
        其中，接下来要选择的元素个数 = k - path.size()，整理得到：
        搜索起点的上界 = n - (k - path.size()) + 1
        所以，我们的剪枝过程就是：把 i <= n 改成 i <= n - (k - path.size()) + 1 ：
        '''
        def dfs_pruning(n,k, begin, path, res):
            if len(path) == k:
                res.append(path[:])
                return
            # 我们的剪枝过程就是：把 i <= n 改成 i <= n - (k - path.size()) + 1 
            for i in range(begin, n - (k - len(path)) + 1 + 1):
                path+=i
                dfs_pruning(n, k, i + 1, path, res)
                path.pop()
        
        # 方法三，在方法二的基础上做了局部改写，思想以及优化都和二一样，可以参考下
        # prefix不用浅拷贝也正确，因为递归传入的是prefix+[remain_selection[i]]，所以存了新的地址，
        # 如果是在之前prefix.append(remain_selection[i])的话就必须得用浅拷贝，因为append只把地址的指向传了进去

        def backtracking(remain_selection,unfinished_count,prefix):
            if unfinished_count==0:
                
                res.append(prefix)
                return
            tmp_length=len(remain_selection)
            for i in range(tmp_length):
                # print("prefix before = ", prefix)
                #此处代码优化可以显著提高运行的效率
                if unfinished_count<=tmp_length-i+1:
                    backtracking(remain_selection[i+1:],unfinished_count-1,prefix+[remain_selection[i]])
                else:
                    break
        
        def dfs_another(cur, n, k):
            pass
            # 这种方法思想就是每一个节点有两种情况，选和不选，由于要考虑的剪枝情况比较多，所以这种反复了解即可。
            

        res = []
        if k <= 0 or n < k or k <=0 :
            return []
        # 从1开始是题目设定的要求
        path = []
        # 方法一
        # dfs(n, k, 1, path, res)
        # 方法二
        # dfs_pruning(n, k, 1, path, res)
        # 方法三：
        # backtracking([i for i in range(1,n+1)],k,path)

        import itertools
        # 其实这个地方可以去看itertools.combinations的实现，因为这个实现在所有提交结果中效率是最高的。
        res = list(itertools.combinations(range(1,n+1),k))
        # 个人猜想是c/c++实现的，然后编译成python的接口。

        return res
# @lc code=end

