#
# @lc app=leetcode.cn id=923 lang=python
#
# [923] 三数之和的多种可能
#

# @lc code=start
class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        counter = dict()
        for num in arr:
            counter[num] = counter.get(num, 0)+ 1
        
        arr = counter.keys()
        arr.sort()
        res = 0

        for i in range(0, len(arr)):
            if arr[i] * 3 == target and counter[arr[i]] > 2:
                res += counter[arr[i]] * (counter[arr[i]] - 1) * (counter[arr[i]] - 2) // 6
            for j in range(i+1, len(arr)):
                if arr[i] * 2 + arr[j] == target and counter[arr[i]] > 1:
                    res += counter[arr[i]] * (counter[arr[i]] - 1) * counter[arr[j]] // 2
                if arr[i] + arr[j] * 2 == target and counter[arr[j]] > 1:
                    res += counter[arr[i]] * counter[arr[j]] * (counter[arr[j]] - 1) // 2
                if target - arr[i] - arr[j] in counter and target - arr[i] - arr[j] > arr[j]: 
                    res += counter[arr[i]] * counter[arr[j]] * counter[target-arr[i]-arr[j]]
                

        return res % 1000000007# @lc code=end

