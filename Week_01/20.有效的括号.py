#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 第一种栈的方法
        # if len(s) %2 == 1:
        #     return False
        # pairs = {
        #     ')' : '(',
        #     '}' : '{',
        #     ']' : '['
        # }
        # # s = '(([[]])){}'
        # stack = list()
        # # 这种方法要考虑的情况比较多。
        # # 后遇到的左括号要先闭合，因此将左括号存入栈中，那么栈顶元素就是最后一个左括号，
        # # 因此当遇到一个右括号时，判断栈顶元素是否与其匹配。
        # for ch in s:
        #     if ch in pairs:
        #         if not stack or pairs[ch] != stack[-1]:
        #             return False
                
        #         stack.pop()

        #     else:
        #         stack.append(ch)
                
        # return  not stack
        # 另外一种栈的方法，更简便更快。
        if len(s) %2 == 1:
            return False
        pairs = {
                '{' : '}',  
                '[' : ']',
                '(' : ')',
                '?' : '?'
            }
        stack = ['?']
        for c in s:
            if c in pairs: 
                stack.append(c)

            elif pairs[stack.pop()] != c :
                # )(
                # 如果有右括号不匹配，直接返回False， 
                # 注意这种方法必须要提前在pairs中放入不相干元素，防止为空。
                return False  
                

        return  len(stack) == 1


            
# @lc code=end
        