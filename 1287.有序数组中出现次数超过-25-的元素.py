#
# @lc app=leetcode.cn id=1287 lang=python
#
# [1287] 有序数组中出现次数超过25%的元素
#

# @lc code=start
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        threshold = len(arr) / 4 + 1
        tmp = 1
        cur = arr[0]

        for n in arr[1:]:
            if n == cur:
                tmp += 1
                if tmp >= threshold:
                    return n
            else:
                cur = n
                tmp = 1
        return cur
            
        
# @lc code=end

