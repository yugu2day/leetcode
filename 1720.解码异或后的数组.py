#
# @lc app=leetcode.cn id=1720 lang=python
#
# [1720] 解码异或后的数组
#

# @lc code=start
class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        res = [first]
        for code in encoded:
            res.append(first ^ code)
            first = first^code
        return res
# @lc code=end

