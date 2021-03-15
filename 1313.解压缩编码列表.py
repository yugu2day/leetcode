#
# @lc app=leetcode.cn id=1313 lang=python
#
# [1313] 解压缩编码列表
#

# @lc code=start
class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums), 2):
            res.extend(nums[i] * [nums[i+1]])
        return res

# @lc code=end

