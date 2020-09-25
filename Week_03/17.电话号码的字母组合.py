#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_key = {
            '2' : ['a', 'b' ,'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r','s'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x','y', 'z']
        }
        # dp
     
        # ans = ['']
        # for num in digits:
        #     ans = [pre + suf for pre in ans  for suf in phone_key[num] ]
        #     print("ans = ", ans)
        # return ans

        # backtrack
        # https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/dian-hua-hao-ma-de-zi-mu-zu-he-by-leetcode-solutio/
        # https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/hui-su-dui-lie-tu-jie-by-ml-zimingmeng/

        def backtrack(comb,nextdigit):
            if len(nextdigit) == 0:
                res.append(comb)
            else:
                for letter in phone_key[nextdigit[0]]:
                    backtrack(comb + letter, nextdigit[1:])

        res = []
        backtrack('',digits)
        return res



# @lc code=end

