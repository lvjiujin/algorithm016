#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        # # 链表问题中要有哑结点的意识（这是一个简单的技巧问题）dummy node
        # dummy = ListNode(0)
        # cur = dummy
        # carry = 0
        # while l1 or l2 or carry or carry:
        #     x = l1.val if l1 else 0
        #     y = l2.val if l2 else 0
        #     sum = x + y + carry
        #     carry = sum // 10
        #     sum %= 10
        #     # cur 指向一个新创建的节点
        #     cur.next = ListNode(sum)
        #     # cur不断指向下一个节点
        #     cur = cur.next
        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        # return dummy.next
        # 方法2：list转化成number，相加后，number转化成List
        # 这种方法貌似比上面那种情况效率高。特别是上面一种情况，当两个list长度差距很大时，还在做很多无用的加法。
        return self.numberToList(self.listToNumber(l1) + self.listToNumber(l2))
        
    def listToNumber(self, node: ListNode) -> int:
        number = 0
        mult = 1
        while node:
            number += mult*node.val
            mult *= 10
            node = node.next
        return number
    
    def numberToList(self, number: int) -> ListNode:
        number, digit = divmod(number, 10)
        node = ListNode(digit)
        head = node        
        while number:
            number, digit = divmod(number, 10)
            node.next = ListNode(digit)
            node = node.next
        return head

# @lc code=end

