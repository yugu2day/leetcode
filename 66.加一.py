#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = len(digits) - 1

        while idx >= 0:
            if digits[idx] + 1 == 10:
                digits[idx] = 0
                idx -= 1
            else:
                digits[idx] += 1
                break
        if idx == -1:
            digits = [1] + digits
        return digits
# @lc code=end

