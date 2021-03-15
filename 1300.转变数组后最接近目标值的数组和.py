#
# @lc app=leetcode.cn id=1300 lang=python
#
# [1300] 转变数组后最接近目标值的数组和
#

# @lc code=start
class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        s = [0]
        for num in arr:
            s.append(s[-1] + num) 
        start = 0
        end = arr[-1]

        while start < end:
            r1, r2 = self.get_num_result(start, s, arr), self.get_num_result(end, s, arr)
            # print start, end, r1, r2

            if r1 == target:
                return start
            if r2 == target:
                return end

            if end - start <= 1:
                if abs(r1 - target) > abs(r2-target):
                    return end
                else:
                    return start

            mid = (start + end) // 2
            r3 = self.get_num_result(mid, s, arr)

            if target == r3:
                return mid
            elif target > r3:
                start = mid if start != mid else mid+1
            else:
                end = mid if end != mid else mid-1

        return start

    def get_num_result(self, num, s, arr):
        for index, n in enumerate(arr):
            if n >= num:
                return s[index] + (len(arr)-index) * num
        return s[-1]

# @lc code=end

