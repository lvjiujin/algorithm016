#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 方法一： 递归
        # if not head or not head.next:
        #     return head
        # ret = self.reverseList(head.next)
        # # 原来1->2-...., 现在反转到2->1.
        # # 当前节点的下一个节点的next指向当前节点（将链表指向反转）
        # head.next.next = head
        # head.next = None
        # return ret
        # 方法二：迭代: 往链表头部添加元素天然具有倒序的特点
        oldNode = head
        newNode = None
        while oldNode:
            # 1. 保存next
            oldNextNode = oldNode.next
            # 2. 修改next
            oldNode.next = newNode
            # 3. 修改newNode
            newNode = oldNode
            # 4. 修改oldNode指向下一个节点
            oldNode = oldNextNode
        return newNode


# @lc code=end

