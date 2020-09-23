# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 方法一 
        # if not head:
        #     return []
        # stack = []
        # while head:
        #     stack.append(head.val)
        #     head = head.next
        # return stack[::-1]
        # 方法二：stack
        # if not head:
        #     return []
        # from collections import deque
        # stack = deque()
        # while head:
        #     stack.append(head.val)
        #     head = head.next
        # res = []
        # while stack:
        #     res.append(stack.pop())

        # return res
        # 方法三递归
        # return self.reversePrint(head.next) + [head.val] if head else []
        # 方法四：
        count = 0
        node = head
        while head:
            head = head.next
            count+=1
        res = [0 for _ in range(count)]
        while node:
            res[count -1] = node.val
            count-=1
            node = node.next
        return res
        
