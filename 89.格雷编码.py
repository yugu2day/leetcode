#
# @lc app=leetcode.cn id=89 lang=python
#
# [89] 格雷编码
#

# @lc code=start
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 对于n, n+1的情况下，在n的每种情况下前面增加0和1
        if n == 0:
            return [0]

        tmp = self.grayCode(n-1)
        return [_ for _ in tmp] + [pow(2, n-1) + _ for _ in tmp][::-1]
# @lc code=end

