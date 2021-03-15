#
# @lc app=leetcode.cn id=1160 lang=python
#
# [1160] 拼写单词
#

# @lc code=start
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        ch_counter = collections.Counter(chars)
        for word in words:
            w = collections.Counter(word)
            for ch, c in w.items():
                if c > ch_counter.get(ch, 0):
                    break
            else:
                res += len(word)
        return res
# @lc code=end

