#
# @lc app=leetcode.cn id=303 lang=python
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = [0]
        for num in nums:
            self.arr.append(self.arr[-1] + num)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.arr[j+1] - self.arr[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

