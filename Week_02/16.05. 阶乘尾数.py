class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 思路:其实n!中的零全部是5和2的倍数贡献的，由于因子为2的个数大于5的，所以，只需计算其中有多少个5的倍数即可。
        if n == 0:
            return 0
        m5 = 0
        while n > 0:
            n = n // 5
            m5 += n
        return m5

def main():
	solu = Solution()
	res = solu.trailingZeroes(5)
	print("res = ", res)

if __name__ == "__main__":
	main()


