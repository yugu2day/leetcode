#
# @lc app=leetcode.cn id=605 lang=python
#
# [605] 种花问题
#

# @lc code=start
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        c = 0
        length = len(flowerbed)
        for idx in range(0, length):
            if flowerbed[idx] == 1:
                continue
            if idx > 0 and flowerbed[idx-1] == 1:
                continue
            if idx < length - 1 and flowerbed[idx+1] == 1:
                continue
            flowerbed[idx] = 1
            c += 1
            if c >= n:
                return True
        return c >= n
        
# @lc code=end

