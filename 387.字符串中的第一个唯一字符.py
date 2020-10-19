#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()
        for index, ch in enumerate(s):
            if ch in dic:
                dic[ch][1] += 1
            else:
                dic[ch] = [index, 1]
        
        min_index = -1
        for ch, [idx, cnt] in dic.items():
            if cnt > 1:
                continue
            if min_index == -1 or idx < min_index:
                min_index = idx
        return min_index
# @lc code=end

