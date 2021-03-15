#
# @lc app=leetcode.cn id=1185 lang=python
#
# [1185] 一周中的第几天
#

# @lc code=start
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        cnt = -1
        for i in range(1971, year):
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 ==0):
                cnt += 366
            else:
                cnt += 365

        
        for i in range(1, month):
            if i in [1,3,5,7,8,10,12]:
                cnt += 31
            elif i in [4,6,9,11]:
                cnt += 30
            elif i==2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 ==0)):
                cnt += 29
            elif i==2:
                cnt += 28

        
        cnt += day
        return week[cnt%7]
# @lc code=end

