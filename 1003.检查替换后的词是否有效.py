#
# @lc app=leetcode.cn id=1003 lang=python
#
# [1003] 检查替换后的词是否有效
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = ""
        for ch in s:
            tmp += ch
            if tmp[-3:] == "abc":
                tmp = tmp[:-3]
        return tmp == ""
# @lc code=end

