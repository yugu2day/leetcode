#
# @lc app=leetcode.cn id=748 lang=python
#
# [748] 最短补全词
#

# @lc code=start
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        l = collections.defaultdict(int)
        for c in licensePlate:
            if c.isalpha():
                l[c.lower()] += 1

        words.sort(key=lambda x:len(x))
        ws = []
        for word in words:
            c = collections.defaultdict(int)
            for char in word:
                c[char] += 1

            for k, v in l.items():
                if v > c.get(k, 0):
                    break
            else:
                return word
        return ""
# @lc code=end

