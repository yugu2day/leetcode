#
# @lc app=leetcode.cn id=740 lang=python
#
# [740] 删除并获得点数
#

# @lc code=start
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        start = 0
        res = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                res += self.rob(nums[start:i])
                start = i

        res += self.rob(nums[start:])
        return res
    

    def rob(self, nums):
        #对nums进行转换
        tmp = 0
        arr = []
        for idx, n in enumerate(nums):
            if idx == 0 or n != nums[idx-1]:
                arr.append(n)
            else:
                arr[-1] += n
                

        if len(arr) <= 2:
            return max(arr)
        dp = [0] * len(arr)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            dp[i] = max(dp[i-2] + arr[i], dp[i-1])
        return dp[-1]
# @lc code=end

