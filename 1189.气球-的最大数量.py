#
# @lc app=leetcode.cn id=1189 lang=python
#
# [1189] “气球” 的最大数量
#

# @lc code=start
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counter = collections.Counter(text)
        return min([counter["b"], counter["a"], counter["l"]/2, counter["o"]/2, counter["n"]])
# @lc code=end

