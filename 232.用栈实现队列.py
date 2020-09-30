#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.p = None


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if not self.s1:
            self.p = x
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        res = self.s1.pop()
        if self.s2:
            self.p = self.s2[-1]
        else:
            self.p = None
        while self.s2:
            self.s1.append(self.s2.pop())
        return res


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.p


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.s1 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

