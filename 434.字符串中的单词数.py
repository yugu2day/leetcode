#
# @lc app=leetcode.cn id=434 lang=python
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([_ for _ in s.split(' ') if _])
# @lc code=end

