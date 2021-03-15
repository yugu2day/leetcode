#
# @lc app=leetcode.cn id=1299 lang=python
#
# [1299] 将每个元素替换为右侧最大元素
#

# @lc code=start
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        cur = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > cur:
                arr[i], cur = cur, arr[i]
            else:
                arr[i] = cur
        arr[-1] = -1
        return arr
# @lc code=end

