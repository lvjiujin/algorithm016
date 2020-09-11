#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#

# @lc code=start
class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next =nextNode

class MyCircularQueue:
    # cycle queue: 入队: 队尾指针read +1, 出队 队头指针 head(front) +1
    # 入队和出队的时候，可以不用取模运算，直接下面这种骚操作：只要没有指向末尾，就加1，否则就为0
    # rear = rear == arr.length - 1 ? 0 : rear + 1; 
    # front = front == arr.length - 1 ? 0 : front + 1; 
    # 判断队列满或空，直接从容量和元素个数来判断，尽量不要用头指针等于尾指针这种非常容易出错。
    # 不太喜欢在数组中也多弄出来一个元素，用来做判满判空。

    # 两种实现策略：数组/链表。
    # 方法一 数组实现循环队列（没有考虑线程锁）

    # def __init__(self, k: int):
    #     """
    #     Initialize your data structure here. Set the size of the queue to be k.
    #     """
    #     self.queue = [0 for _ in range(k)]
    #     self.headIndex = 0
    #     self.count = 0
    #     self.capacity = k
    #     # 觉得还是弄一个尾指针方便些。头指针和尾指针相差count-1个位置。

    # def enQueue(self, value: int) -> bool:
    #     """
    #     Insert an element into the circular queue. Return true if the operation is successful.
    #     """
    #     if self.count == self.capacity:
    #         return False
    #     self.queue[(self.headIndex + self.count) % self.capacity] = value
    #     self.count+=1
    #     return True

    # def deQueue(self) -> bool:
    #     """
    #     Delete an element from the circular queue. Return true if the operation is successful.
    #     """
    #     if self.count == 0:
    #         return False
    #     self.headIndex = (self.headIndex + 1) % self.capacity
    #     self.count -= 1
    #     return True
        

    # def Front(self) -> int:
    #     """
    #     Get the front item from the queue.
    #     """
    #     if self.count == 0:
    #         return -1
    #     return self.queue[self.headIndex]

    # def Rear(self) -> int:
    #     """
    #     Get the last item from the queue.
    #     """
    #     # empty queue
    #     if self.count == 0:
    #         return -1
    #     return self.queue[(self.headIndex + self.count -1) %self.capacity]

    # def isEmpty(self) -> bool:
    #     """
    #     Checks whether the circular queue is empty or not.
    #     """
    #     return self.count == 0
        

    # def isFull(self) -> bool:
    #     """
    #     Checks whether the circular queue is full or not.
    #     """
    #     return self.count == self.capacity

    # 方法二：链表：
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.head = None
        self.count = 0
        self.tail = None

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        
        self.count+=1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        
        self.head = self.head.next
        self.count -= 1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # empty queue
        if self.count == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity

    # 两种方法 time complexity O(1)
    # space complexity O(n) # 因为要创建一个新的队列， 链表效率更高。


# Your MyCircularQueue object will be instantiated and called as such:
# k = 5
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(5)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# print("param_1 = ", param_1)
# print("param_2 = ", param_2)
# print("param_3 = ", param_3)
# print("param_4 = ", param_4)
# print("param_5 = ", param_5)
# print("param_6 = ", param_6)
# @lc code=end

