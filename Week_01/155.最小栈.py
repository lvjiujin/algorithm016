#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:
    # 方法一：采用辅助栈的方法，辅助栈在每次入栈的时候，存储min(辅助栈的栈顶元素, x) 的最小值，这样保证每一个入栈的元素a都有一个最小值和他对应。
    # 这种做法的好处是当出栈后，min_stack中栈顶的元素依然是当前栈的最小元素。
    # 时间复杂度O（1）， 空间复杂度为O（n)。
    # 方法二：不用辅助栈，而是将栈中每一个元素设计为一个tuple(x, min_value) tuple中第一个元素是当前要push的值，min_value 是当前栈中的最小值。
    # 原理和第一种方法其实是一样的。都借用了这样一种思想：栈中每一个元素对应一个最小值，一一对应的关系。
    def __init__(self):
        """
        initialize your data structure here.
        """
        import math
        self.stack = []
        self.min_stack = [math.inf]


    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]

    # 方法二:
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, self.stack[-1][1]))
        
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        
            
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return None
    '''



# Your MinStack object will be instantiated and called as such:
# x = 10
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

