#
# @lc app=leetcode.cn id=719 lang=python
#
# [719] 找出第 k 小的距离对
#

# @lc code=start
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def IsValid(gap):
            l, cnt = 0, 0
            for idx, r in enumerate(nums):
                while r - nums[l] > gap:
                    l += 1
                cnt = cnt + (idx - l)
            return cnt >= k
                

        # 二分查找排序后的diff
        nums.sort()

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if IsValid(mid):
                right = mid
            else:
                left = mid + 1
        return left

        
# @lc code=end

