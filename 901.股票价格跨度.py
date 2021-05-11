#
# @lc app=leetcode.cn id=901 lang=python
#
# [901] 股票价格跨度
#

# @lc code=start
class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.day = 0
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        while self.stack:
            if self.stack[-1][0] <= price:
                self.stack.pop()
            else:
                break
        if self.stack:
            gap = self.day - self.stack[-1][1]
        else:
            gap = self.day + 1

        self.stack.append([price, self.day])
        self.day += 1
        return gap

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

