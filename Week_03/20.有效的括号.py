#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 方法一：最朴素的一种做法，也就是最基本的方法要会要熟练，不然的话，万一高大上紧张写不出怎么办？

        # if s == "":
        #     return True
        # if len(s) % 2 == 1:
        #     return False
        # while "()" in s or "{}" in s or "[]" in s:
        #     if "()" in s:
        #         s = s.replace("()","")
        #     if "[]" in s:
        #         s = s.replace("[]","")
        #     if "{}" in s:
        #         s = s.replace("{}", "")
        
        # if s == "":
        #     return True
        # else:
        #     return False

        # 方法二：stack, 复习，强化，过遍数
        # 注意这种方法必须要提前在pairs 和stack 中放入不相干元素，防止为空。
        if len(s) % 2 == 1:
            return False
        pairs = {
            '[': ']',
            '{': '}',
            '(': ')',
            '?': '?'
        }
        stack = ['?']
        for c in s:
            if c in pairs:
                stack.append(c)
            elif pairs[stack.pop()] != c:
                return False
        
        return  len(stack) == 1
# @lc code=end

