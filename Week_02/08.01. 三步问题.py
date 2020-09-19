import numpy as np
class Solution:
    def waysToStep(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2) + f(n-3)
        """
        要考察动态规划，主要是考察为什么可以在过程中取模而不影响最终结果，（python）只在最终return的结果上取模就超时了
        状态转移方程不用说了：S(n) = S(n-1)+S(n-2)+S(n-3)
        因为要对结果S(n)取模，用S(n)'代S(n)取模的结果，即 if S(n) > 1000000007: S(n)'= S(n) - n1000000007
        于是如果对S(n+1)取模有：S(n+1) = S(n) + S(n-1) + S(n-2) = S(n)' + n1000000007 + S(n-1) + S(n-2)
        S(n+1) % 1000000007 = ( S(n)' + S(n-1) + S(n-2) ) % 1000000007
        所以即使在中间取模也不影响结果

        https://leetcode-cn.com/problems/three-steps-problem-lcci/solution/san-bu-wen-ti-zhong-jian-guo-cheng-zhong-qu-mo-er-/

        """
        f = [1,2,4]
        if n <4:
            return f[n-1]
        f1, f2, f3, f4 = 1, 2, 4, 0
        # 非常重要的思想：中间结果取模不影响最终结果
        for i in range(4,n+1):
            f4 = (f1 + f2 + f3) % 1000000007
            f1 = f2
            f2 = f3
            f3 = f4
        return f4
    def waysToStep2(self, n: int) -> int:
        # 矩阵快速幂, 斐波那契数列的经典方法
        self.p = int(1e9+7)
        f = [1, 2, 4]
        if n <= 3: 
            return f[n-1]
        # 最最重要的是要找到这样的一个矩阵A，如何找到的呢？
        A = np.array([[0, 0, 1], [1, 0, 1], [0, 1, 1]], dtype=np.int64)
        B = self.mat_pow(A, n-3)
        res = 0
        for i in range(3):
            res += f[i] * B[i][2]
        return int(res%self.p)
    
    def mat_pow(self, A, n):
        m = A.shape[0]
        B = np.eye(m, dtype=np.int64)
        while n > 0:
            if (n&1)!=0:
                B = np.mod(np.matmul(B, A), self.p).astype(np.int64)
            A = np.mod(np.matmul(A, A), self.p).astype(np.int64)
            n >>= 1
        return B;

        

def main():
    solu = Solution()
    x = solu.waysToStep(63)
    print(x)

if __name__ == '__main__':
    main()