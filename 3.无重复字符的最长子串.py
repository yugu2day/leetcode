#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 1
        res = 0

        while right <= len(s):
            if right < len(s) and s[right] not in s[left:right]:
                res = max(res, right-left+1)
                right += 1
            else:
                left += 1
                if left >= len(s):
                    break
        return res
# @lc code=end

