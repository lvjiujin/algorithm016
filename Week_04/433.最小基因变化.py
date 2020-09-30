#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # possible=["A","C","G","T"]
        # queue=[(start, 0, 0)]
        # pos = 0
        # while queue:
        #     # print("queue = ", queue)
        #     # 广度优先遍历模板
        #     (word, step)=queue.pop(0)
        #     if word ==end:
        #         return step
            
        #     for i in range(len(word)):
        #         for p in possible:
        #             # 从第0个位置开始匹配新的字符串
        #             temp=word[:i]+p+word[i+1:]  
        #             # 在bank里面就处理(set中in操作复杂度是0(1))
        #             if temp in bank: 
        #                 # 从bank里移除，避免重复计数
        #                 bank.remove(temp)  
        #                 # 加入队列，步数加1
        #                 queue.append((temp,step+1)) 
        # return -1

        # 上述的一个改进点是将possbile 列表，转化成字典，这样少了一次循环操作。
        # 当前字符没必要替换成自己。

        possible_dict = {
                        "A": "CGT",
                        "C": "AGT",
                        "G": "ACT",
                        "T": "ACG"
                    }
        queue=[(start,0)]
        while queue:
            # print("queue = ", queue)
            # 广度优先遍历模板
            (word, step)=queue.pop(0)
            if word ==end:
                return step
            
            for i, c  in enumerate(word):
                
                for p in possible_dict[c]:
                    # 从第0个位置开始匹配新的字符串
                    temp=word[:i]+p+word[i+1:]
                    
                    # 在bank里面就处理(set中in操作复杂度是0(1))
                    if temp in bank: 
                        # 从bank里移除，避免重复计数
                        bank.remove(temp)  
                        # 加入队列，步数加1
                        queue.append((temp,step+1)) 
        return -1
        # 继续改进:
        # 在经过判断是否在基因库中后 又还原了原字符串 只是将临时重组且符合基因库的重组字符串加入队列而已
        # 上述改造暂告失败，先放一放。
        
# @lc code=end

