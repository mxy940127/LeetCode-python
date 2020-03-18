#Author:mxy940127
# -*- coding:utf-8 -*-
#  @Author   : Eric.Miao


"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_one = []
        self.stack_two = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_one.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_one:
            return None
        while self.stack_one:
            self.stack_two.append(self.stack_one.pop())
        res = self.stack_two.pop()
        while self.stack_two:
            self.stack_one.append(self.stack_two.pop())
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack_one:
            return None
        return self.stack_one[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if len(self.stack_one) > 0 else True
