# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    size = 0
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 方法一：用栈的思想：
        # if not head :
        #     return head
        # if k == 0:
        #     return None
        # from collections import deque
        # stack = deque()
        # while head:
        #     stack.append(head)
        #     head = head.next
        # node = None
        # while k>0:
        #     node = stack.pop()
        #     k-=1
        # return node

        # 方法二：双指针法, 两个循环
        # 主要思想：不同步的双指针法，一个先走k步，另一个才开始走，先走的那个指针到达终点，那么后面的指针刚好到达倒数第k个位置。
        # if not head :
        #     return head
        # if k == 0:
        #     return None
        # p = head
        # while k > 0:
        #     p, k = p.next, k - 1
        # while p:
        #     p, head = p.next, head.next
        # return head
        # 方法三：双指针，单循环（增加一个计数变量）
        # if not head :
        #     return head
        # if k == 0:
        #     return None
        # t, p = 0, head
        # while p:
        #     if t>=k:
        #         head = head.next
        #     p = p.next
        #     t+=1
        # return head

        # 方法四：递归：之前做过，过遍数，加强记忆和理解
        if not head:
            return head
        node = self.getKthFromEnd(head.next,k)
        # 上面那句递归调用的代码，在head不为空之前是不返回的，也就是node一直为空，也就是下面的这个过程“递推，一直推到底”，
        # 当head为空后，开始return 有值，也就是node开始被赋值，也就是回归的过程
        # 先递推走到末尾，然后回归的过程中，size ++, 直到size==k的时候，把head进行返回。
        # 在递推走到末尾前，递归函数调用自己的地方（也就是这行代码：self.getKthFromEnd(head.next,k)）后面的代码不执行。
        self.size+=1
        if self.size == k:
            return head
        return node

                

