#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        # 方法一：迭代法
        a, b, c = 1, 0, 0
        for _ in range(n): 
            a, b, c = b, c, a + b + c
        return c

   
        # f0, f1, f2 = 0, 1, 1
        # return self.tri(n, f0, f1, f2)
        
        # 方法二：尾递归
        """
        由于编译器的优化，当方法调用出现在函数末尾时，没有其它操作要执行，编译器在编译代码时，就不会开辟新的栈空间，而是直接覆盖当前栈执行。根据此思路使用尾递归进行求解，当递归到n==0时，就可得到对应的解。
        https://leetcode-cn.com/problems/n-th-tribonacci-number/solution/wei-di-gui-by-creammangopie/

        """
        # 方法三：矩阵快速幂
        # 这种方法比较麻烦
    def tri(self, n, res1, res2, res3):
        if n <= 0:
            return res1
        
        return self.tri(n - 1, res2, res3, res1 + res2 + res3)
    


        
# @lc code=end

