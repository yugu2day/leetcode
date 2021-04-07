#
# @lc app=leetcode.cn id=1078 lang=python
#
# [1078] Bigram 分词
#

# @lc code=start
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text = text.split(' ')
        res = []
        for i in range(0, len(text) - 2):
            if text[i] == first and text[i+1] == second:
                res.append(text[i+2])
        return res
# @lc code=end

