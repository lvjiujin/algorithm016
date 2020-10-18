#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 哑结点的应用
        if not head:
            return None
        dummpy = ListNode(0, head)
        slow, fast = head, dummpy
        while slow and fast:
            if n > 0:
                slow = slow.next
                n -= 1
            else:
                slow = slow.next
                fast = fast.next
            
        node = fast.next.next
        fast.next = node
        return dummpy.next
        
# @lc code=end

