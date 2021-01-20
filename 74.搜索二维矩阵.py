#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = [row[0] for row in matrix]
        exist, pos = self.binarySearch(rows, target)
        # print exist, pos
        if exist == True:
            return True
        exist, pos = self.binarySearch(matrix[pos], target)
        return exist
    
    def binarySearch(self, arr ,target):
        """
        找到最后一个小于或等于target的位置
        """
        start, end = 0, len(arr) - 1
        res = 0
        while start <= end:
            mid = (start + end) // 2
            if target == arr[start]:
                return True, start
            if target == arr[end]:
                return True, end
            if target == arr[mid]:
                return True, mid

            if target > arr[mid]:
                res = mid
                start = mid + 1
            if target < arr[mid]:
                end = mid - 1
        return False, res
# @lc code=end

