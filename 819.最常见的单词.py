#
# @lc app=leetcode.cn id=819 lang=python
#
# [819] 最常见的单词
#

# @lc code=start
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        c = ["!", "?", "'", ",", ";", "."]
        paragraph = paragraph.lower()
        for i in c:
            paragraph = paragraph.replace(i, " ")
        paragraph = paragraph.split(' ')

        counter = collections.Counter(paragraph)
        for k, v in counter.most_common():
            if k and k not in banned:
                return k
# @lc code=end

