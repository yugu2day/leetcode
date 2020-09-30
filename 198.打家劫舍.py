#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # dp[i][0] 表示不抢该房屋 dp[i][1]表示抢劫该房屋
        dp = [[0,0] for _ in range(len(nums))]
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for index, num in enumerate(nums):
            if index == 0:
                continue
            dp[index][0] = max(dp[index-1][0], dp[index-1][1])
            dp[index][1] = dp[index-1][0]+num
        return max(dp[-1][0], dp[-1][1])


# @lc code=end

