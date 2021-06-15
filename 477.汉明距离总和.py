#
# @lc app=leetcode.cn id=477 lang=python
#
# [477] 汉明距离总和
#

# @lc code=start
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        flag = False
        res = 0
        while not flag:
            flag = True
            tmp = 0
            for index, num in enumerate(nums):
                if flag and num > 0:
                    flag = False
                if num & 1 != 0:
                    tmp += 1
                nums[index] >>= 1
            res += tmp * (n - tmp)
        
        return res
# @lc code=end

