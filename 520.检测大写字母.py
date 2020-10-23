#
# @lc app=leetcode.cn id=520 lang=python
#
# [520] 检测大写字母
#

# @lc code=start
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False

        
# @lc code=end

