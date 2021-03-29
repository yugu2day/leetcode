#
# @lc app=leetcode.cn id=632 lang=python
#
# [632] 最小区间
#

# @lc code=start
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        arr = []
        # 记录数和index， 并按数值排序
        for i in range(0, len(nums)):
            for num in nums[i]:
                arr.append([i, num])

        arr = sorted(arr, key=lambda x:x[1])
        # print arr

        l = 0
        r = l + len(nums)
        res = [arr[0][1], arr[-1][1]]

        # 动态维护各层数是否存在
        pos = [0] * len(nums)
        for [i, n] in arr[l:r]:
            pos[i] += 1

        while l < len(arr) and r <= len(arr):
            # print arr[l], arr[r-1]
            if all(pos):
                if arr[r-1][1] - arr[l][1] < res[1] - res[0]:
                    res = [arr[l][1], arr[r-1][1]]
                pos[arr[l][0]] -= 1
                l += 1

            else:
                if r < len(arr):
                    pos[arr[r][0]] += 1
                r += 1
        return res 
# @lc code=end

