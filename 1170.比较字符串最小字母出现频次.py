#
# @lc app=leetcode.cn id=1170 lang=python
#
# [1170] 比较字符串最小字母出现频次
#

# @lc code=start
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
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

