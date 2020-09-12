#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # hash 法:
        # 思路:
        # 首先，我们分配一个 Set 去保存所有的列表节点。我们逐一遍历列表，检查当前节点是否出现过，
        # 如果节点已经出现过，那么一定形成了环且它是环的入口。否则如果有其他点是环的入口，
        # 我们应该先访问到其他节点而不是这个节点。其他情况，没有成环则直接返回 null 
        # node_set = set()
        # node = head
        # while node:
        #     if node in node_set:
        #         return node
        #     else:
        #         node_set.add(node)
            
        #     node = node.next
        
        # return None

        # time complexity O(n), space complexity O(n)
        # 快慢指针法： 
        # 这个神奇的写法 time complexity O(n) space complexity O(1)
        #  the first loop detects the cycle and the second loop gives the node where the cycle starts. 
        slow = fast = head
        # 第一个loop 找到相遇点， 第二个loop找到环的入口。
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head
        
        
# @lc code=end

