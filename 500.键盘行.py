#
# @lc app=leetcode.cn id=500 lang=python
#
# [500] 键盘行
#

# @lc code=start
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = {'q','w','e','r','t','y','u','i','o','p'}
        set2 = {'a','s','d','f','g','h','j','k','l'}
        set3 = {'z','x','c','v','b','n','m'}
        res = []
        for word in words:
            w_set = set(list(word.lower()))
            if w_set - set1 == set() or w_set - set2 == set() or w_set - set3 == set():
                res.append(word)
        return res
# @lc code=end

