#
# @lc app=leetcode.cn id=888 lang=python
#
# [888] 公平的糖果棒交换
#

# @lc code=start
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sa, sb = sum(A), sum(B)

        equal = (sa + sb) // 2

        gap = abs(equal - sa)

        set_a, set_b = set(A), set(B)
        for i in set_a:
            if sa < sb and i + gap in set_b:
                return [i, i+gap]
            if sa > sb and i - gap in set_b:
                return [i, i-gap]
# @lc code=end

