#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
class deNode:
    def __init__(self, val, prev=None, next=None):
        self.value = val
        self.prev = prev
        self.next = next

class MyCircularDeque:
    # 值得注意的一点是：
    # 定义循环变量 front 和 rear 。一直保持这个定义，到底是先赋值还是先移动指针就很容易想清楚了。

    # front：指向队列头部第 1 个有效数据的位置；
    # rear：指向队列尾部（即最后 1 个有效数据）的下一个位置，即下一个从队尾入队元素的位置。
    # 队列的头指针和尾指针有一点不同，头指针指向头部的第一个元素，尾指针指向尾部的最后一个元素的下一个位置。
    # 所以在操作的时候要特别注意些。

    '''
    另一种判断队列为满的条件：需要在__init__中多分配一个空间。
    浪费一个位置是指：循环数组中任何时刻一定至少有一个位置不存放有效元素。

    判别队列为空的条件是：front == rear;

    判别队列为满的条件是：(rear + 1) % capacity == front;。
    可以这样理解，当 rear 循环到数组的前面，要从后面追上 front，还差一格的时候，判定队列为满。
    '''
    # 第一种方法：数组法
    # def __init__(self, k: int):
    #     """
    #     Initialize your data structure here. Set the size of the deque to be k.
    #     """
    #     self.capacity = k
    #     self.front = 0
    #     self.rear = 0
    #     self.dequeue = [0 for _ in range(k)]
    #     self.count = 0


    # def insertFront(self, value: int) -> bool:
    #     """
    #     Adds an item at the front of Deque. Return true if the operation is successful.
    #     """
    #     if self.count == self.capacity:
    #         return False
    #     self.dequeue[(self.front -1) % self.capacity] = value
    #     # 还有一种写法是下面这样子，其实感觉没必要加上capacity,因为取模了。
    #     # self.front = (self.front - 1 + self.capacity) % self.capacity
    #     self.front = (self.front - 1) % self.capacity
    #     self.count += 1
    #     return True

    # def insertLast(self, value: int) -> bool:
    #     """
    #     Adds an item at the rear of Deque. Return true if the operation is successful.
    #     """
    #     if self.count == self.capacity:
    #         return False
    #     self.dequeue[self.rear] = value
    #     self.rear = (self.rear + 1) % self.capacity
    #     self.count += 1
    #     return True

    # def deleteFront(self) -> bool:
    #     """
    #     Deletes an item from the front of Deque. Return true if the operation is successful.
    #     """
    #     if self.count == 0:
    #         return False
    #     self.front = (self.front + 1) % self.capacity
    #     self.count -= 1
    #     return True

    # def deleteLast(self) -> bool:
    #     """
    #     Deletes an item from the rear of Deque. Return true if the operation is successful.
    #     """
    #     if self.count == 0:
    #         return False
    #     self.rear = (self.rear - 1) % self.capacity
    #     self.count -= 1
    #     return True

    # def getFront(self) -> int:
    #     """
    #     Get the front item from the deque.
    #     """
    #     if self.count == 0:
    #         return -1
    #     return self.dequeue[self.front]

    # def getRear(self) -> int:
    #     """
    #     Get the last item from the deque.
    #     """
    #     if self.count == 0:
    #         return -1
    #     return self.dequeue[(self.rear -1) % self.capacity] 

    # def isEmpty(self) -> bool:
    #     """
    #     Checks whether the circular deque is empty or not.
    #     """
    #     return self.count == 0

    # def isFull(self) -> bool:
    #     """
    #     Checks whether the circular deque is full or not.
    #     """
        
    #     return self.count == self.capacity
    # 第二种方法：链表法
    #  第二种方法终于搞明白了，参考：
    # https://leetcode.com/problems/design-circular-deque/discuss/234378/python-simple-solution-easy-to-understand
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.head = deNode(0)
        self.tail = deNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        node = deNode(value)

        self._addNode(self.head, node)
        
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        node = deNode(value)
        
        self._addNode(self.tail.prev, node)

        self.count += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        
        nxt = self.head.next.next 
        self.head.next = nxt 
        nxt.prev = self.head

        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        
        prev = self.tail.prev.prev 
        self.tail.prev = prev
        prev.next = self.tail

        self.count -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.count == 0:
            return -1
        return self.head.next.value

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.count == 0:
            return -1
        return self.tail.prev.value

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        
        return self.count == self.capacity
    
    def _addNode(self, node, add_node):
        nxt = node.next 
        node.next = add_node
        add_node.prev = node
        add_node.next = nxt
        nxt.prev = add_node

        
        

    

# Your MyCircularDeque object will be instantiated and called as such:
# k = 5
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(1)
# param_2 = obj.insertFront(2)
# param_2 = obj.insertFront(3)
# param_5 = obj.getFront()
# print("head.val = ", obj.head.v )

# print("param_5 = ", param_5)
# param_3 = obj.deleteFront()
# param_3 = obj.insertLast(5)
# param_3 = obj.insertLast(6)
# param_3 = obj.getRear()
# print("param_5 = ", param_3)
# param_4 = obj.deleteLast()

# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

# @lc code=end

