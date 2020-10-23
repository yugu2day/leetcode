#
# @lc app=leetcode.cn id=551 lang=python
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return True if (s.count('A')<=1 and 'LLL' not in s) else False
        
# @lc code=end

