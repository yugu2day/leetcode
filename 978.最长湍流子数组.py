#
# @lc app=leetcode.cn id=978 lang=python
#
# [978] 最长湍流子数组
#

# @lc code=start
class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) <= 1:
            return len(arr)
        # 滑动窗口
        while len(arr) >= 2 and arr[0] == arr[1]:
            arr.pop(0)

        if len(arr) < 2:
            return 1

        idx = 0
        res = 1
        flag = arr[1] < arr[0]
        
        for i in range(1, len(arr) - 1):
            if arr[i+1] > arr[i] and flag:
                flag = False
                continue
            if arr[i+1] < arr[i] and not flag:
                flag = True
                continue

            res = max(res, i - idx + 1)
            tmp = i
            while tmp < len(arr) - 2 and arr[tmp] == arr[tmp+1]:
                tmp += 1
            # print i, idx
            idx = tmp 
            flag = arr[idx+1] < arr[idx] 
        return max(res, len(arr) - idx)
# @lc code=end

