#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
            # 递归。
            # ans = []
            # def backtrack(S, left, right):
            #     if len(S) == 2 * n:
            #         ans.append(''.join(S))
            #         return
            #     if left < n:
            #         S.append('(')
            #         backtrack(S, left+1, right)
            #         S.pop()
            #     if right < left:
            #         S.append(')')
            #         backtrack(S, left, right+1)
            #         S.pop()
            # backtrack([], 0, 0)
            # return ans
            # amazing solution 
            dp = [[] for i in range(n + 1)]
            dp[0].append('')
            for i in range(n + 1):
                for j in range(i):
                    dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
                    print("d[{}] = {}".format(i, dp[i]))
            return dp[n]
            '''
            ['xyz'] + ['yyyz'] = ['xyz', 'yyyz']
            https://leetcode.com/problems/generate-parentheses/discuss/10369/Clean-Python-DP-Solution
            you could see in the code that x represents one j-pair solution and y represents one (i - j - 1) pair solution, 
            and we are taking into account all possible of combinations of them)
            d[1] = ['()']
            " +
            "d[2] = ['()()']
            " +
            "d[2] = ['()()', '(())']
            " +
            "d[3] = ['()()()', '()(())']
            " +
            "d[3] = ['()()()', '()(())', '(())()']
            " +
            "d[3] = ['()()()', '()(())', '(())()', '(()())', '((()))']
            '''
        


# @lc code=end

