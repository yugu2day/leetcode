#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs = sorted(strs, key=lambda x:-len(x))
        tmp = strs[0]

        while tmp:
            for s in strs:
                if s.startswith(tmp):
                    continue
                else:
                    tmp = tmp[:-1]
                    break
            else:
                return tmp
        return ""


# @lc code=end

