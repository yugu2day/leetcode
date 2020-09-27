#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min_s = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        if not self.min_s or x <= self.min_s[-1]:
            self.min_s.append(x)

    def pop(self):
        """
        :rtype: None
        """
        n = self.s.pop()
        if n == self.min_s[-1]:
            self.min_s.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_s[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

