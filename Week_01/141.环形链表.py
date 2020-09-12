#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 方法一，hash法，类似于之前两数之和的做法。
        # 这种方法 time complexity O(n) space complexity O(n)
        # if not head:
        #     return False
        # nodeset = set()
        # node = head
        # while node:
        #     if node in nodeset:
        #         return True
        #     else:
        #         nodeset.add(node)
            
        #     node = node.next

        # return False
        # 方法二：快慢指针法:
        # 记住这种搞法，龟兔赛跑
        fast_point, slow_point = head, head 
        while fast_point:
            if fast_point.next and fast_point.next.next:
                fast_point = fast_point.next.next
                slow_point = slow_point.next
            else:
                
                return False
            
            if fast_point == slow_point:
                return True
            
        return False


            
        
        
# @lc code=end

