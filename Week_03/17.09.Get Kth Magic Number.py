class Solution:
    '''
    Design an algorithm to find the kth number such that the only prime factors are 3, 5, and 7. 
    Note that 3, 5, and 7 do not have to be factors, but it should not have any other prime factors.
    For example, the first several multiples would be (in order) 1, 3, 5, 7, 9, 15, 21.

    '''
    def getKthMagicNumber(self, k: int) -> int:
        num = 1
        p3, p5, p7 = 0, 0, 0
        i = 0
        dp = [0 for _ in range(k)]
        dp[0] = 1
        for i in range(1,k):
            dp[i] = min(dp[p3] * 3, dp[p5] * 5, dp[p7] * 7)
            if dp[i] == dp[p3]*3:
                p3+=1
            if dp[i] == dp[p5]*5:
                p5+=1
            if dp[i] == dp[p7]*7:
                p7+=1
        
        return dp[k-1]

            
def main():
    mysolu = Solution()
    k = 5
    result = mysolu.getKthMagicNumber(k)
    print("result = ", result)

if __name__ == "__main__":
    main()