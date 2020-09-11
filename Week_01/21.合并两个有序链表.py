#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 方法一、递归
        if l1 and l2:
            if l1.val > l2.val :
                l1, l2 = l2, l1
            # Make sure l1 is alway the smaller 
            l1.next = self.mergeTwoLists(l1.next, l2)
        
        return l1 or l2

            
        # 为什么我每次感觉递归都难以理解，而且自己想不到呢。
        #     
        # 方法二、迭代
        # prevhead = ListNode(-1) # 哑结点
        # prev = prevhead
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         prev.next = l1
        #         l1 = l1.next
        #     else:
        #         prev.next = l2
        #         l2 = l2.next
        #     prev = prev.next
        
        # prev.next = l1 if l1 is not None else l2
        # # 因为prevhead的头结点是哑结点要去掉，所以从下一个节点开始
        # return prevhead.next
        
# @lc code=end

