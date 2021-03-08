#
# @lc app=leetcode.cn id=1011 lang=python
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left = 1
        right = sum(weights)
        res = -1
        while left <= right:
            guess = (left + right) // 2

            # 满足
            if self.confirm(guess, weights, D):
                res = guess
                right = guess - 1
            else:
                left = guess + 1

        return res
    
    def confirm(self, guess, weights, D):
        day = 1
        tmp = 0
        for n in weights:
            if n > guess:
                return False
            tmp += n

            if tmp > guess:
                tmp = n
                day += 1
        return day <= D if tmp <= guess else day + 1 <= D
# @lc code=end

