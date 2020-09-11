#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 用递归法
        # https://lyl0724.github.io/2020/01/25/1/
        """
        找终止条件：本题终止条件很明显，当递归到链表为空或者链表只剩一个元素的时候，没得交换了，自然就终止了。
        找返回值：返回给上一层递归的值应该是已经交换完成后的子链表。
        单次的过程：因为递归是重复做一样的事情，所以从宏观上考虑，只用考虑某一步是怎么完成的。
        我们假设待交换的俩节点分别为head和node，node应该接受上一级返回的子链表(参考第2步)。
        就相当于是一个含三个节点的链表交换前两个节点，就很简单了，想不明白的画画图就ok。
        """
        if not head or not head.next:
            return head
        # 一共三个节点:head, node, swapPairs(node.next)
      	# 下面的任务便是交换这3个节点中的前两个节点
        node = head.next
        head.next = self.swapPairs(node.next)
        node.next = head 
        return node 


# @lc code=end

