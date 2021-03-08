#
# @lc app=leetcode.cn id=914 lang=python
#
# [914] 卡牌分组
#

# @lc code=start
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # 计数后的最大公约数
        d = dict()
        for num in deck:
            d[num] = d.get(num, 0) + 1
        
        return reduce(self.get_res, d.values()) >= 2

    def get_res(self, a, b):
        while b != 0:
            a, b = b, a%b
        return a
# @lc code=end

