#
# @lc app=leetcode.cn id=729 lang=python
#
# [729] 我的日程安排表 I
#

# @lc code=start
class MyCalendar(object):

    def __init__(self):
        self.arr = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.arr:
            self.arr.append([start, end])
            return True
        
        for idx, item in enumerate(self.arr):
            if (start >= item[0] and start < item[1]) or (end > item[0] and end <= item[1]) or (start <= item[0] and end >= item[1]):
                return False
            if end <= item[0]:
                self.arr.insert(idx, [start, end])
                return True
        
        self.arr.append([start, end])
        return True

        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

