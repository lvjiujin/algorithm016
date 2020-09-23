class Solution:
    def replaceSpace(self, s: str) -> str:
    	# 方法一
        # return s.replace(" ","%20")
        # 方法二：
        # res = ""
        # for c in s:
        #     if c == " ":
        #         res+="%20"
        #     else:
        #         res+=c
        # return res
        # 方法三：
        return '%20'.join(s.split(' '))
        
