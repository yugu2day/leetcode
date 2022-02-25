#
# @lc app=leetcode.cn id=2160 lang=python
#
# [2160] 拆分数位后四位数字的最小和
#

# @lc code=start
class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr = list(str(num))
        arr.sort()

        return int(arr[0]+arr[3]) + int(arr[1]+arr[2])
# @lc code=end

