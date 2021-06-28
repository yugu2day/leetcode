#
# @lc app=leetcode.cn id=1624 lang=python
#
# [1624] 两个相同字符之间的最长子字符串
#

# @lc code=start
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = collections.defaultdict(list)
        res = -1
        for idx, ch in enumerate(s):
            if len(pos[ch]) > 0:
                res = max(res, idx - pos[ch][0] - 1)
            pos[ch].append(idx)
        return res
# @lc code=end

