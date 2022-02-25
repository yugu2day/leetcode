#
# @lc app=leetcode.cn id=2114 lang=python
#
# [2114] 句子中的最多单词数
#

# @lc code=start
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return max(len(s.split(' ')) for s in sentences)
# @lc code=end

