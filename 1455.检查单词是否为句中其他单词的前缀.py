#
# @lc app=leetcode.cn id=1455 lang=python
#
# [1455] 检查单词是否为句中其他单词的前缀
#

# @lc code=start
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        s = sentence.split(' ')
        for idx, word in enumerate(s):
            if word.startswith(searchWord):
                return idx + 1
        return -1
# @lc code=end

