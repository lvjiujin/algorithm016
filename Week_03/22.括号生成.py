#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        # 左括号随便加，只要不超标
        # 左括号》右括号的时候，才能添加右括号。
        # 自顶向下的编程风格
        # result = []
        # self._generate(0, 0, n, "", result)
        # return result

        # 另一种神奇的方法，过遍数，加强肌肉记忆。
        # 主要思想就是：s = '( + x + ')' + y , x可以是多层括号嵌套，y也是。x和y的下标安排的很巧妙
        '''
        https://leetcode.com/problems/generate-parentheses/discuss/10369/Clean-Python-DP-Solution
        To generate all n-pair parentheses, we can do the following:

        1. Generate one pair: ()

        2. Generate 0 pair inside, n - 1 afterward: () (...)...

        3. Generate 1 pair inside, n - 2 afterward: (()) (...)...

            ...

            Generate n - 1 pair inside, 0 afterward: ((...))
        (you could see in the code that x represents one j-pair solution and y represents one (i - j - 1) pair solution, 
        and we are taking into account all possible of combinations of them
        '''
        result = [[] for _ in range(n + 1)]
        result[0].append('')
        for i in range(n + 1):
            for j in range(i):
                result[i] += ['(' + x + ')' + y for x in result[j] for y in result[i - j -1]]
        
        return result[n]

    def _generate(self, left, right, n, s, result):
        # the number of left parathesis equals to right parathesis, terminal the recursion.
        if left == n and right == n:
            result.append(s)
            return
        # 左括号只要不超标，随便加。
        if left < n:
            self._generate(left + 1, right, n, s + "(", result)
        # 只要左括号大于右括号，右括号随便加
        if left > right:
            self._generate(left, right + 1, n, s + ")", result)


# def main():
#     solu = Solution()
#     result = solu.generateParenthesis(3)
#     print("result = ", result )

            
# @lc code=end

