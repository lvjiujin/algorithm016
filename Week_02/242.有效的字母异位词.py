#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        # 方法一：就最普通的hash 字典方法
        # from collections import defaultdict
        # d1 = defaultdict(lambda :0) # 设置不存在时，默认值为0
        # for i in s:
        #     d1[i] +=1
        # for i in t:
        #     d1[i]-=1
        # for x in set(d1.values()):
        #     if x !=0:
        #         return False
        
        # return True
        # 方法二，利用a-z 26个字母的范围的ascii，将ascii的范围限制在0~25. 字符-'a' 
        # record = [0 for _ in range(26)]
        # ord convert the char character to interger. 97 represent the alpha 'a'
        # https://leetcode-cn.com/problems/valid-anagram/solution/242-you-xiao-de-zi-mu-yi-wei-ci-shu-zu-zai-ha-xi-f/
        for i in range(len(s)):
            record[ord(s[i]) - 97] +=1
            record[ord(t[i]) - 97] -=1
        
        for x in record:
            if x !=0:
                return False
        return True



# @lc code=end

