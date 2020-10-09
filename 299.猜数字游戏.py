#
# @lc app=leetcode.cn id=299 lang=python
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dic_s = dict()
        dic_g = dict()
        a, b = 0, 0
        for index in range(0, len(secret)):
            dic_s[secret[index]] = dic_s.get(secret[index], 0) + 1
            dic_g[guess[index]] = dic_g.get(guess[index], 0) + 1
            if secret[index] == guess[index]:
                a += 1
        for k, v in dic_s.items():
            b += min(v, dic_g.get(k, 0))
        return "{}A{}B".format(a,b-a)
# @lc code=end

